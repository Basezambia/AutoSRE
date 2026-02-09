import json
import os
from dataclasses import dataclass
from pathlib import Path
from typing import List

from dotenv import load_dotenv
from pydantic import BaseModel

from autosre_ai.models import ActionType


@dataclass(frozen=True)
class AutoSREConfig:
    approval_required: List[ActionType]
    risk_threshold: float
    shadow_pipeline_required: bool


class AppSettings(BaseModel):
    database_path: Path = Path("data/autosre.db")
    log_level: str = "INFO"
    host: str = "127.0.0.1"
    port: int = 8000


def load_config(path: Path) -> AutoSREConfig:
    raw = json.loads(path.read_text())
    approval_required = [ActionType(item) for item in raw["approval_required"]]
    return AutoSREConfig(
        approval_required=approval_required,
        risk_threshold=float(raw["risk_threshold"]),
        shadow_pipeline_required=bool(raw["shadow_pipeline_required"]),
    )


def load_settings() -> AppSettings:
    load_dotenv(override=False)
    return AppSettings(
        database_path=Path(os.getenv("AUTOSRE_DATABASE_PATH", "data/autosre.db")),
        log_level=os.getenv("AUTOSRE_LOG_LEVEL", "INFO"),
        host=os.getenv("AUTOSRE_HOST", "127.0.0.1"),
        port=int(os.getenv("AUTOSRE_PORT", "8000")),
    )
