import json
from dataclasses import dataclass
from pathlib import Path
from typing import List

from autosre_ai.models import ActionType


@dataclass(frozen=True)
class AutoSREConfig:
    approval_required: List[ActionType]
    risk_threshold: float
    shadow_pipeline_required: bool


def load_config(path: Path) -> AutoSREConfig:
    raw = json.loads(path.read_text())
    approval_required = [ActionType(item) for item in raw["approval_required"]]
    return AutoSREConfig(
        approval_required=approval_required,
        risk_threshold=float(raw["risk_threshold"]),
        shadow_pipeline_required=bool(raw["shadow_pipeline_required"]),
    )
