from pathlib import Path

from fastapi.testclient import TestClient

from autosre_ai.app import create_app


def test_healthz(tmp_path: Path, monkeypatch) -> None:
    monkeypatch.setenv("AUTOSRE_DATABASE_PATH", str(tmp_path / "autosre.db"))
    app = create_app()
    client = TestClient(app)

    response = client.get("/healthz")
    assert response.status_code == 200
    assert response.json() == {"status": "ok"}


def test_simulate_and_approve(tmp_path: Path, monkeypatch) -> None:
    monkeypatch.setenv("AUTOSRE_DATABASE_PATH", str(tmp_path / "autosre.db"))
    app = create_app()
    client = TestClient(app)

    simulate_response = client.post("/api/incidents/simulate")
    assert simulate_response.status_code == 200
    incidents = simulate_response.json()
    assert len(incidents) == 3

    pending = next((item for item in incidents if item["status"] == "pending"), None)
    if pending:
        approve_response = client.post(f"/api/approve/{pending['id']}")
        assert approve_response.status_code == 200
        assert approve_response.json()["status"] == "approved"
