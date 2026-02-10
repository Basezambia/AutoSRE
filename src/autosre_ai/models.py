from dataclasses import dataclass
from enum import Enum
from typing import Dict, List


class EventType(str, Enum):
    BUILD_FAILURE = "build_failure"
    LATENCY_SPIKE = "latency_spike"
    SLO_RISK = "slo_risk"


class ActionType(str, Enum):
    SCALE = "scale"
    RESTART = "restart"
    CONFIG_PATCH = "config_patch"
    HOTFIX_PR = "hotfix_pr"
    SHADOW_PIPELINE = "shadow_pipeline"


@dataclass(frozen=True)
class SignalEvent:
    event_type: EventType
    service: str
    severity: float
    metadata: Dict[str, str]


@dataclass
class ActionPlan:
    actions: List[ActionType]
    summary: str
    risk_score: float
