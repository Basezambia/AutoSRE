from dataclasses import dataclass
from datetime import datetime, timezone
from uuid import uuid4


@dataclass
class IncidentRecord:
    id: str
    event_type: str
    service: str
    severity: float
    summary: str
    actions: list[str]
    risk_score: float
    status: str
    created_at: str
    updated_at: str

    @classmethod
    def from_plan(
        cls,
        *,
        event_type: str,
        service: str,
        severity: float,
        summary: str,
        actions: list[str],
        risk_score: float,
        status: str,
    ) -> "IncidentRecord":
        now = datetime.now(timezone.utc).isoformat()
        return cls(
            id=str(uuid4()),
            event_type=event_type,
            service=service,
            severity=severity,
            summary=summary,
            actions=actions,
            risk_score=risk_score,
            status=status,
            created_at=now,
            updated_at=now,
        )
