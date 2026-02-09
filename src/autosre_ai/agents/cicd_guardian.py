from autosre_ai.models import ActionPlan, ActionType, SignalEvent


class CiCdGuardian:
    """Agent responsible for CI/CD automation and pipeline health."""

    def plan(self, event: SignalEvent) -> ActionPlan:
        summary = (
            f"CI/CD Guardian detected {event.event_type.value} for {event.service}. "
            "Propose fix via Copilot Coding Agent and validate in shadow pipeline."
        )
        actions = [ActionType.HOTFIX_PR, ActionType.SHADOW_PIPELINE]
        risk_score = min(1.0, event.severity + 0.1)
        return ActionPlan(actions=actions, summary=summary, risk_score=risk_score)
