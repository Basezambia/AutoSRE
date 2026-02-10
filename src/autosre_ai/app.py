import logging
from pathlib import Path
from typing import List

from fastapi import FastAPI, HTTPException, Request
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from pydantic import BaseModel

from autosre_ai.agents.orchestrator import Orchestrator
from autosre_ai.config import load_config, load_settings
from autosre_ai.schemas import IncidentRecord
from autosre_ai.service import IncidentService
from autosre_ai.storage import IncidentRepository


class IncidentResponse(BaseModel):
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


def create_app() -> FastAPI:
    settings = load_settings()
    logging.basicConfig(level=settings.log_level)

    app = FastAPI(title="AutoSRE AI", version="0.2.0")

    repository = IncidentRepository(settings.database_path)
    config = load_config(Path("configs/sample-config.json"))
    orchestrator = Orchestrator(config)
    service = IncidentService(orchestrator, repository)

    base_dir = Path(__file__).resolve().parent
    templates = Jinja2Templates(directory=str(base_dir / "templates"))
    app.mount("/static", StaticFiles(directory=base_dir / "static"), name="static")

    @app.get("/healthz")
    def healthz() -> dict:
        return {"status": "ok"}

    @app.get("/", response_class=HTMLResponse)
    def index(request: Request) -> HTMLResponse:
        return templates.TemplateResponse("index.html", {"request": request})

    @app.get("/api/incidents", response_model=list[IncidentResponse])
    def list_incidents() -> List[IncidentResponse]:
        return [IncidentResponse(**incident.__dict__) for incident in service.list_incidents()]

    @app.post("/api/incidents/simulate", response_model=list[IncidentResponse])
    def simulate_incidents() -> List[IncidentResponse]:
        incidents = service.simulate_incidents()
        return [IncidentResponse(**incident.__dict__) for incident in incidents]

    @app.post("/api/approve/{incident_id}", response_model=IncidentResponse)
    def approve_incident(incident_id: str) -> IncidentResponse:
        incident = service.approve_incident(incident_id)
        if incident is None:
            raise HTTPException(status_code=404, detail="Incident not found")
        return IncidentResponse(**incident.__dict__)

    return app


app = create_app()
