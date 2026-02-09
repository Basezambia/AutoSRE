from pathlib import Path

from autosre_ai.agents.orchestrator import Orchestrator
from autosre_ai.config import load_config
from autosre_ai.models import EventType, SignalEvent
from autosre_ai.service import IncidentService
from autosre_ai.storage import IncidentRepository


def main() -> None:
    config = load_config(Path("configs/sample-config.json"))
    orchestrator = Orchestrator(config)
    repository = IncidentRepository(Path("data/autosre.db"))
    service = IncidentService(orchestrator, repository)

    events = [
        EventType.BUILD_FAILURE,
        EventType.LATENCY_SPIKE,
        EventType.SLO_RISK,
    ]

    for event_type in events:
        event = SignalEvent(
            event_type=event_type,
            service="checkout-service",
            severity=0.7,
            metadata={"source": "simulator"},
        )
        incident = service.create_incident(event)
        print("---")
        print(f"Event: {incident.event_type}")
        print(f"Plan: {incident.summary}")
        print(f"Actions: {incident.actions}")
        print(f"Risk: {incident.risk_score}")
        print(f"Status: {incident.status}")


if __name__ == "__main__":
    main()
