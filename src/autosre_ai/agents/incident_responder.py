from autosre_ai.models import ActionPlan, ActionType, SignalEvent


class IncidentResponder:
    """Agent responsible for incident detection and remediation."""

    def plan(self, event: SignalEvent) -> ActionPlan:
        summary = (
            f"Incident Responder correlates telemetry for {event.service} and "
            "recommends immediate mitigation."
        )
        if event.severity > 0.8:
            actions = [ActionType.SCALE, ActionType.RESTART]
        else:
            actions = [ActionType.CONFIG_PATCH]
        risk_score = min(1.0, event.severity + 0.2)
        return ActionPlan(actions=actions, summary=summary, risk_score=risk_score)
