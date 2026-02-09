import argparse
from pathlib import Path

from autosre_ai.config import load_config
from autosre_ai.models import EventType, SignalEvent
from autosre_ai.agents.orchestrator import Orchestrator


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description="AutoSRE AI demo CLI")
    parser.add_argument(
        "--config",
        type=Path,
        default=Path("configs/sample-config.json"),
        help="Path to AutoSRE config JSON",
    )
    parser.add_argument("--event", type=str, default="build_failure")
    parser.add_argument("--service", type=str, default="api-gateway")
    parser.add_argument("--severity", type=float, default=0.6)
    return parser


def main() -> None:
    parser = build_parser()
    args = parser.parse_args()
    config = load_config(args.config)
    orchestrator = Orchestrator(config)

    event = SignalEvent(
        event_type=EventType(args.event),
        service=args.service,
        severity=args.severity,
        metadata={"source": "demo"},
    )

    plan = orchestrator.route(event)
    plan = orchestrator.apply_policy(plan)

    print("--- AutoSRE AI Plan ---")
    print(f"Event: {event.event_type.value}")
    print(f"Service: {event.service}")
    print(f"Summary: {plan.summary}")
    print(f"Actions: {[action.value for action in plan.actions]}")
    print(f"Risk score: {plan.risk_score}")
    print(f"Requires approval: {orchestrator.requires_approval(plan)}")


if __name__ == "__main__":
    main()
