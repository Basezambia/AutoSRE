import random
from pathlib import Path

from autosre_ai.agents.orchestrator import Orchestrator
from autosre_ai.config import load_config
from autosre_ai.models import EventType, SignalEvent


def main() -> None:
    config = load_config(Path("configs/sample-config.json"))
    orchestrator = Orchestrator(config)

    events = [
        EventType.BUILD_FAILURE,
        EventType.LATENCY_SPIKE,
        EventType.SLO_RISK,
    ]

    for event_type in events:
        event = SignalEvent(
            event_type=event_type,
            service="checkout-service",
            severity=round(random.uniform(0.4, 0.95), 2),
            metadata={"source": "simulator"},
        )
        plan = orchestrator.apply_policy(orchestrator.route(event))
        print("---")
        print(f"Event: {event.event_type.value}")
        print(f"Plan: {plan.summary}")
        print(f"Actions: {[action.value for action in plan.actions]}")
        print(f"Risk: {plan.risk_score}")


if __name__ == "__main__":
    main()
