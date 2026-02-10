from autosre_ai.agents.cicd_guardian import CiCdGuardian
from autosre_ai.agents.incident_responder import IncidentResponder
from autosre_ai.agents.reliability_forecaster import ReliabilityForecaster
from autosre_ai.config import AutoSREConfig
from autosre_ai.models import ActionPlan, ActionType, EventType, SignalEvent


class Orchestrator:
    """Routes signals to specialized agents and enforces approval policy."""

    def __init__(self, config: AutoSREConfig) -> None:
        self.config = config
        self.cicd_guardian = CiCdGuardian()
        self.incident_responder = IncidentResponder()
        self.reliability_forecaster = ReliabilityForecaster()

    def route(self, event: SignalEvent) -> ActionPlan:
        if event.event_type == EventType.BUILD_FAILURE:
            return self.cicd_guardian.plan(event)
        if event.event_type == EventType.LATENCY_SPIKE:
            return self.incident_responder.plan(event)
        if event.event_type == EventType.SLO_RISK:
            return self.reliability_forecaster.plan(event)
        raise ValueError(f"Unsupported event type: {event.event_type}")

    def requires_approval(self, plan: ActionPlan) -> bool:
        return any(action in self.config.approval_required for action in plan.actions)

    def apply_policy(self, plan: ActionPlan) -> ActionPlan:
        if (
            self.config.shadow_pipeline_required
            and ActionType.SHADOW_PIPELINE not in plan.actions
        ):
            plan.actions.append(ActionType.SHADOW_PIPELINE)
        return plan
