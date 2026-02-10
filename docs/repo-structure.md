# Repo Structure

```
AutoSRE/
├── configs/
│   └── sample-config.json
├── docs/
│   ├── agents.md
│   ├── architecture.md
│   ├── demo-scope.md
│   └── repo-structure.md
├── scripts/
│   └── simulate_events.py
├── src/
│   └── autosre_ai/
│       ├── __init__.py
│       ├── agents/
│       │   ├── __init__.py
│       │   ├── cicd_guardian.py
│       │   ├── incident_responder.py
│       │   ├── orchestrator.py
│       │   └── reliability_forecaster.py
│       ├── app.py
│       ├── cli.py
│       ├── config.py
│       ├── models.py
│       ├── schemas.py
│       ├── service.py
│       ├── storage.py
│       ├── static/
│       │   ├── app.js
│       │   └── styles.css
│       └── templates/
│           └── index.html
├── .gitignore
├── pyproject.toml
└── README.md
```
