import random
from typing import List

from autosre_ai.agents.orchestrator import Orchestrator
from autosre_ai.models import EventType, SignalEvent
from autosre_ai.schemas import IncidentRecord
from autosre_ai.storage import IncidentRepository


class IncidentService:
    def __init__(self, orchestrator: Orchestrator, repository: IncidentRepository) -> None:
        self.orchestrator = orchestrator
        self.repository = repository

    def list_incidents(self) -> List[IncidentRecord]:
        return self.repository.list_incidents()

    def get_incident(self, incident_id: str) -> IncidentRecord | None:
        return self.repository.get_incident(incident_id)

    def approve_incident(self, incident_id: str) -> IncidentRecord | None:
        return self.repository.update_status(incident_id, status="approved")

    def create_incident(self, event: SignalEvent) -> IncidentRecord:
        plan = self.orchestrator.apply_policy(self.orchestrator.route(event))
        status = "pending" if self.orchestrator.requires_approval(plan) else "approved"
        record = IncidentRecord.from_plan(
            event_type=event.event_type.value,
            service=event.service,
            severity=event.severity,
            summary=plan.summary,
            actions=[action.value for action in plan.actions],
            risk_score=plan.risk_score,
            status=status,
        )
        return self.repository.create_incident(record)

    def simulate_incidents(self) -> List[IncidentRecord]:
        incidents = []
        for event_type in [EventType.BUILD_FAILURE, EventType.LATENCY_SPIKE, EventType.SLO_RISK]:
            severity = round(random.uniform(0.4, 0.95), 2)
            event = SignalEvent(
                event_type=event_type,
                service="demo-service",
                severity=severity,
                metadata={"source": "api"},
            )
            incidents.append(self.create_incident(event))
        return incidents


