# Minimal Demo Scope (That Still Wins)

## Goals

* Demonstrate **agentic CI/CD automation**, **incident response**, and **reliability engineering**.
* Keep demo runtime light while proving the architecture.

## Demo components

1. **Signal ingestion simulator**
   * Emits: failed build, latency spike, SLO risk.

2. **Orchestrator**
   * Routes each event to the right agent.

3. **Agent actions**
   * CI/CD Guardian → generates a mock PR plan.
   * Incident Responder → chooses scale/restart/config patch.
   * Reliability Forecaster → predicts risk and triggers preemptive action.

4. **Approval step**
   * High-risk actions are blocked until approved.

5. **Summary report**
   * Final summary shows all actions taken and risk scores.

## What you can show in a live demo

* **Real-time event ingestion** with structured logs.
* **Agent routing decisions** and proposed remediations.
* **Human approvals** for critical actions.
* **End-to-end loop** for each of the three requirement categories.
