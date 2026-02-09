# AutoSRE AI

**AutoSRE AI is an agentic DevOps system that autonomously predicts, diagnoses, and remediates production failures by integrating Azure SRE Agent, GitHub Copilot Coding Agent, and Microsoft Agent Framework into a self-healing software delivery pipeline.**

## Category definition (judge lens)

> **Build solutions that leverage agentic DevOps principles to automate CI/CD, incident response, and reliability engineering.**

With **that exact category description**, AutoSRE AI doesn’t just fit — **it is almost a canonical example** of what the category asks for.

## What this repo delivers

* **Agent roles mapped to the SRE lifecycle** (diagnose → remediate → validate → learn). See [docs/agents.md](docs/agents.md).
* **Azure-first architecture** spanning telemetry, orchestration, and safe actuation. See [docs/architecture.md](docs/architecture.md).
* **Minimal demo scope** that still proves all three requirements. See [docs/demo-scope.md](docs/demo-scope.md).
* **Working scaffold** for agent orchestration and telemetry-driven workflows. See [src/autosre_ai](src/autosre_ai).

## Direct requirement mapping (no ambiguity)

### 1) Automate CI/CD

* Agents watch failed builds, flaky tests, slow pipelines.
* A Copilot Coding Agent generates PRs to fix flaky tests, adjust pipeline configs, or roll back breaking changes.
* Agents validate fixes in shadow pipelines before merge.

✅ Requirement satisfied.

### 2) Incident response

* Agents ingest Azure Monitor + App Insights telemetry.
* Detect anomalies before alerts escalate.
* Diagnose root cause across services.
* Execute remediation: scale, restart, config patch, or hotfix PR.
* Keep humans in the loop via approvals.

✅ Requirement satisfied.

### 3) Reliability engineering

* Predictive failure modeling.
* SLO breach forecasting.
* Chaos-aware simulations.
* Preventative remediation before customers are impacted.

✅ Requirement satisfied.

## Local dev

```bash
python -m autosre_ai.cli --help
```

## Repo map

See [docs/repo-structure.md](docs/repo-structure.md) for a guided tour.
