# AutoSRE AI

AutoSRE AI is a **production-ready agentic DevOps platform** that **predicts, diagnoses, and remediates production failures** by coordinating specialized agents for CI/CD automation, incident response, and reliability engineering.

It is not a helper for DevOps teams—it is an **autonomous reliability layer** that can detect issues, generate fixes, and safely execute remediation with human approvals.

## What it is

AutoSRE AI combines:

- **Azure SRE Agent** for incident detection and diagnostics.
- **GitHub Copilot Coding Agent** for automated remediation PRs.
- **Microsoft Agent Framework** for multi-agent orchestration.

The platform continuously monitors telemetry, predicts SLO risk, and drives automated response workflows with full auditability.

## Who it is for

- **SRE and Platform teams** who want autonomous incident response and reduced MTTR.
- **DevOps and CI/CD owners** who need proactive pipeline remediation and reliability guardrails.
- **Engineering leadership** who need measurable improvements to reliability and delivery velocity.

## Primary use cases

- Automatically fix flaky tests and unstable pipelines before they block releases.
- Detect and remediate incidents (scale, restart, patch, or hotfix PRs).
- Forecast SLO risk and execute preemptive mitigation to avoid customer impact.

---

## Features

- **Agentic orchestration** with specialized roles for CI/CD, incidents, and reliability forecasting.
- **Production-grade API** with health checks and structured logging.
- **Web UI** for real-time incident and remediation tracking.
- **Human-in-the-loop approvals** for high-impact actions.
- **Configurable policies** (risk thresholds, approvals, shadow pipeline rules).

---

## Quickstart

### 1) Install dependencies

```bash
python -m venv .venv
source .venv/bin/activate
pip install -e .
```

### 2) Run the API server

```bash
autosre-ai serve
```

### 3) Open the web UI

Visit: `http://127.0.0.1:8000`

### 4) Simulate incidents

```bash
autosre-ai simulate
```

### 5) Run with Docker

```bash
docker build -t autosre-ai .
docker run --rm -p 8000:8000 autosre-ai
```

---

## API endpoints

- `GET /healthz` — health check
- `GET /api/incidents` — list incidents
- `POST /api/incidents/simulate` — generate demo incidents
- `POST /api/approve/{incident_id}` — approve high-risk actions

---

## Configuration

AutoSRE AI uses environment variables for production configuration:

```bash
AUTOSRE_DATABASE_PATH=data/autosre.db
AUTOSRE_LOG_LEVEL=INFO
AUTOSRE_HOST=0.0.0.0
AUTOSRE_PORT=8000
```

You can copy `.env.example` to `.env` and update values as needed.

---

## Architecture

> **Build solutions that leverage agentic DevOps principles to automate CI/CD, incident response, and reliability engineering.**

AutoSRE AI is a canonical example of this category:

- **Automates CI/CD** by repairing flaky tests and validating shadow pipelines.
- **Automates incident response** with diagnostics + remediation.
- **Delivers reliability engineering** with forecasting and preemptive action.

More details:

- [Architecture](docs/architecture.md)
- [Agent Roles](docs/agents.md)
- [Demo Scope](docs/demo-scope.md)
- [Repo Map](docs/repo-structure.md)

---

## Local development

```bash
# Run unit tests
pytest

# Run the API server with reload
uvicorn autosre_ai.app:app --reload
```
