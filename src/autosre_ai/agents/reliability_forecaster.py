from autosre_ai.models import ActionPlan, ActionType, SignalEvent


class ReliabilityForecaster:
    """Agent responsible for SLO risk prediction and preventative actions."""

    def plan(self, event: SignalEvent) -> ActionPlan:
        summary = (
            f"Reliability Forecaster predicts SLO risk for {event.service} and "
            "triggers preventative remediation."
        )
        actions = [ActionType.SCALE]
        risk_score = min(1.0, event.severity + 0.15)
        return ActionPlan(actions=actions, summary=summary, risk_score=risk_score)
