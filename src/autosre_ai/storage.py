import json
import sqlite3
from dataclasses import asdict
from datetime import datetime, timezone
from pathlib import Path
from typing import List, Optional

from autosre_ai.schemas import IncidentRecord


class IncidentRepository:
    def __init__(self, database_path: Path) -> None:
        self.database_path = database_path
        self.database_path.parent.mkdir(parents=True, exist_ok=True)
        self._init_db()

    def _connect(self) -> sqlite3.Connection:
        return sqlite3.connect(self.database_path)

    def _init_db(self) -> None:
        with self._connect() as conn:
            conn.execute(
                """
                CREATE TABLE IF NOT EXISTS incidents (
                    id TEXT PRIMARY KEY,
                    event_type TEXT NOT NULL,
                    service TEXT NOT NULL,
                    severity REAL NOT NULL,
                    summary TEXT NOT NULL,
                    actions TEXT NOT NULL,
                    risk_score REAL NOT NULL,
                    status TEXT NOT NULL,
                    created_at TEXT NOT NULL,
                    updated_at TEXT NOT NULL
                )
                """
            )

    def list_incidents(self) -> List[IncidentRecord]:
        with self._connect() as conn:
            rows = conn.execute(
                "SELECT id, event_type, service, severity, summary, actions, risk_score, status, created_at, updated_at FROM incidents ORDER BY created_at DESC"
            ).fetchall()
        return [self._row_to_record(row) for row in rows]

    def get_incident(self, incident_id: str) -> Optional[IncidentRecord]:
        with self._connect() as conn:
            row = conn.execute(
                "SELECT id, event_type, service, severity, summary, actions, risk_score, status, created_at, updated_at FROM incidents WHERE id = ?",
                (incident_id,),
            ).fetchone()
        if row is None:
            return None
        return self._row_to_record(row)

    def create_incident(self, record: IncidentRecord) -> IncidentRecord:
        payload = asdict(record)
        payload["actions"] = json.dumps(payload["actions"])
        with self._connect() as conn:
            conn.execute(
                """
                INSERT INTO incidents (id, event_type, service, severity, summary, actions, risk_score, status, created_at, updated_at)
                VALUES (:id, :event_type, :service, :severity, :summary, :actions, :risk_score, :status, :created_at, :updated_at)
                """,
                payload,
            )
        return record

    def update_status(self, incident_id: str, status: str) -> Optional[IncidentRecord]:
        updated_at = datetime.now(timezone.utc).isoformat()
        with self._connect() as conn:
            conn.execute(
                "UPDATE incidents SET status = ?, updated_at = ? WHERE id = ?",
                (status, updated_at, incident_id),
            )
        return self.get_incident(incident_id)

    @staticmethod
    def _row_to_record(row: sqlite3.Row) -> IncidentRecord:
        return IncidentRecord(
            id=row[0],
            event_type=row[1],
            service=row[2],
            severity=row[3],
            summary=row[4],
            actions=json.loads(row[5]),
            risk_score=row[6],
            status=row[7],
            created_at=row[8],
            updated_at=row[9],
        )
