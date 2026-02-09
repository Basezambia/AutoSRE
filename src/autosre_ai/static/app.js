const cards = document.getElementById("cards");
const refreshBtn = document.getElementById("refresh");
const simulateBtn = document.getElementById("simulate");

async function fetchIncidents() {
  const response = await fetch("/api/incidents");
  const data = await response.json();
  renderIncidents(data);
}

async function simulateIncidents() {
  const response = await fetch("/api/incidents/simulate", { method: "POST" });
  const data = await response.json();
  renderIncidents(data.concat(await (await fetch("/api/incidents")).json()));
}

async function approveIncident(id) {
  await fetch(`/api/approve/${id}`, { method: "POST" });
  await fetchIncidents();
}

function renderIncidents(incidents) {
  cards.innerHTML = "";
  incidents.forEach((incident) => {
    const card = document.createElement("article");
    card.className = "card";
    card.innerHTML = `
      <div class="card-header">
        <h2>${incident.service}</h2>
        <span class="status ${incident.status}">${incident.status.toUpperCase()}</span>
      </div>
      <p><strong>Event:</strong> ${incident.event_type}</p>
      <p><strong>Summary:</strong> ${incident.summary}</p>
      <p><strong>Actions:</strong> ${incident.actions.join(", ")}</p>
      <p><strong>Risk score:</strong> ${incident.risk_score}</p>
      <p><strong>Severity:</strong> ${incident.severity}</p>
      <div class="card-footer">
        <small>Created: ${new Date(incident.created_at).toLocaleString()}</small>
        ${incident.status === "pending" ? `<button data-id="${incident.id}">Approve</button>` : ""}
      </div>
    `;
    const approveButton = card.querySelector("button");
    if (approveButton) {
      approveButton.addEventListener("click", () => approveIncident(incident.id));
    }
    cards.appendChild(card);
  });
}

refreshBtn.addEventListener("click", fetchIncidents);
simulateBtn.addEventListener("click", simulateIncidents);

fetchIncidents();
