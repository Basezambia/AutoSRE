import argparse
from pathlib import Path

import uvicorn

from autosre_ai.config import load_config, load_settings
from autosre_ai.models import EventType, SignalEvent
from autosre_ai.agents.orchestrator import Orchestrator
from autosre_ai.service import IncidentService
from autosre_ai.storage import IncidentRepository


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description="AutoSRE AI command line")
    subparsers = parser.add_subparsers(dest="command", required=True)

    serve_parser = subparsers.add_parser("serve", help="Run the AutoSRE AI API server")
    serve_parser.add_argument("--host", type=str, default=None)
    serve_parser.add_argument("--port", type=int, default=None)

    simulate_parser = subparsers.add_parser("simulate", help="Simulate incidents")
    simulate_parser.add_argument(
        "--config",
        type=Path,
        default=Path("configs/sample-config.json"),
        help="Path to AutoSRE config JSON",
    )
    simulate_parser.add_argument("--event", type=str, default="build_failure")
    simulate_parser.add_argument("--service", type=str, default="api-gateway")
    simulate_parser.add_argument("--severity", type=float, default=0.6)

    return parser


def run_server(host: str | None, port: int | None) -> None:
    settings = load_settings()
    uvicorn.run(
        "autosre_ai.app:app",
        host=host or settings.host,
        port=port or settings.port,
        reload=False,
    )


def run_simulation(config_path: Path, event: str, service: str, severity: float) -> None:
    config = load_config(config_path)
    orchestrator = Orchestrator(config)
    repository = IncidentRepository(Path("data/autosre.db"))
    service_layer = IncidentService(orchestrator, repository)

    signal = SignalEvent(
        event_type=EventType(event),
        service=service,
        severity=severity,
        metadata={"source": "cli"},
    )

    plan = orchestrator.apply_policy(orchestrator.route(signal))
    status = "pending" if orchestrator.requires_approval(plan) else "approved"
    incident = service_layer.create_incident(signal)

    print("--- AutoSRE AI Plan ---")
    print(f"Event: {signal.event_type.value}")
    print(f"Service: {signal.service}")
    print(f"Summary: {plan.summary}")
    print(f"Actions: {[action.value for action in plan.actions]}")
    print(f"Risk score: {plan.risk_score}")
    print(f"Requires approval: {status == 'pending'}")
    print(f"Incident ID: {incident.id}")


def main() -> None:
    parser = build_parser()
    args = parser.parse_args()

    if args.command == "serve":
        run_server(args.host, args.port)
        return

    if args.command == "simulate":
        run_simulation(args.config, args.event, args.service, args.severity)
        return


if __name__ == "__main__":
    main()
