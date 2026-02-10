# AutoSRE AI Agent Roles

## Orchestrator (Control Plane)

* Coordinates multi-agent workflows.
* Routes signals to the right agent by intent.
* Applies global policy (risk thresholds, approvals, SLAs).

## Incident Responder

* Detects anomalies before alert escalation.
* Correlates telemetry across services.
* Proposes and executes remediation actions (scale, restart, config patch).

## CI/CD Guardian

* Monitors failed builds, flaky tests, and regressions.
* Uses Copilot Coding Agent to produce PRs.
* Validates fixes via shadow pipelines before merge.

## Reliability Forecaster

* Predicts SLO breach risk.
* Runs chaos-aware simulations.
* Triggers preventative remediation.

## Human-in-the-loop Approver

* Reviews high-risk actions.
* Ensures compliance and auditability.
