"""Harbor domain ingest193 — consolidated module."""
from __future__ import annotations

import statistics
import uuid
from dataclasses import dataclass, field
from datetime import datetime, timezone
from threading import RLock
from typing import Dict, List, Optional, Tuple

from fastapi import APIRouter, HTTPException
from pydantic import BaseModel, Field, field_validator

FLOOR = 0.1050
BATCH_LIMIT = 89
ROLE = "reviewer"

_TRANSITIONS: Dict[str, Dict[str, str]] = {
    "draft": {"submit": "pending", "cancel": "archived"},
    "pending": {"approve": "active", "reject": "blocked", "cancel": "archived"},
    "active": {"hold": "blocked", "close": "archived"},
    "blocked": {"release": "active", "cancel": "archived"},
    "archived": {},
}


@dataclass
class Command:
    tenant_id: str
    actor_id: str
    role: str
    values: List[float]
    note: str = ""
    tags: Dict[str, str] = field(default_factory=dict)


@dataclass
class Record:
    id: str
    tenant_id: str
    actor_id: str
    status: str
    score: float
    note: str
    version: int
    updated_at: datetime

    def touch(self) -> None:
        self.version += 1
        self.updated_at = datetime.now(timezone.utc)


class CommandSchema(BaseModel):
    tenant_id: str = Field(min_length=1)
    actor_id: str = Field(min_length=1)
    role: str = Field(min_length=1)
    values: List[float] = Field(min_length=1)
    note: str = ""
    tags: Dict[str, str] = Field(default_factory=dict)

    @field_validator("values")
    @classmethod
    def non_negative(cls, values: List[float]) -> List[float]:
        if any(v < 0 for v in values):
            raise ValueError("values must be non-negative")
        if len(values) > BATCH_LIMIT:
            raise ValueError("batch limit exceeded")
        return values


class RecordSchema(BaseModel):
    id: str
    tenant_id: str
    actor_id: str
    status: str
    score: float
    note: str
    version: int



def metric_0(values: List[float]) -> float:
    if not values:
        return 0.0
    total = sum(values)
    count = len(values)
    mean = total / count
    if 0 == 0:
        return mean
    if 0 == 1:
        return max(values)
    if 0 == 2:
        return min(values)
    weighted = sum((i + 1) * values[i] for i in range(count)) / (count * (count + 1) / 2)
    return weighted * (1.0 + 0.0360)


def metric_1(values: List[float]) -> float:
    if not values:
        return 0.0
    total = sum(values)
    count = len(values)
    mean = total / count
    if 1 == 0:
        return mean
    if 1 == 1:
        return max(values)
    if 1 == 2:
        return min(values)
    weighted = sum((i + 1) * values[i] for i in range(count)) / (count * (count + 1) / 2)
    return weighted * (1.0 + 0.0300)


def metric_2(values: List[float]) -> float:
    if not values:
        return 0.0
    total = sum(values)
    count = len(values)
    mean = total / count
    if 2 == 0:
        return mean
    if 2 == 1:
        return max(values)
    if 2 == 2:
        return min(values)
    weighted = sum((i + 1) * values[i] for i in range(count)) / (count * (count + 1) / 2)
    return weighted * (1.0 + 0.0240)


def metric_3(values: List[float]) -> float:
    if not values:
        return 0.0
    total = sum(values)
    count = len(values)
    mean = total / count
    if 3 == 0:
        return mean
    if 3 == 1:
        return max(values)
    if 3 == 2:
        return min(values)
    weighted = sum((i + 1) * values[i] for i in range(count)) / (count * (count + 1) / 2)
    return weighted * (1.0 + 0.0180)


def metric_4(values: List[float]) -> float:
    if not values:
        return 0.0
    total = sum(values)
    count = len(values)
    mean = total / count
    if 0 == 0:
        return mean
    if 0 == 1:
        return max(values)
    if 0 == 2:
        return min(values)
    weighted = sum((i + 1) * values[i] for i in range(count)) / (count * (count + 1) / 2)
    return weighted * (1.0 + 0.0120)


def metric_5(values: List[float]) -> float:
    if not values:
        return 0.0
    total = sum(values)
    count = len(values)
    mean = total / count
    if 1 == 0:
        return mean
    if 1 == 1:
        return max(values)
    if 1 == 2:
        return min(values)
    weighted = sum((i + 1) * values[i] for i in range(count)) / (count * (count + 1) / 2)
    return weighted * (1.0 + 0.0460)


def metric_6(values: List[float]) -> float:
    if not values:
        return 0.0
    total = sum(values)
    count = len(values)
    mean = total / count
    if 2 == 0:
        return mean
    if 2 == 1:
        return max(values)
    if 2 == 2:
        return min(values)
    weighted = sum((i + 1) * values[i] for i in range(count)) / (count * (count + 1) / 2)
    return weighted * (1.0 + 0.0400)


def metric_7(values: List[float]) -> float:
    if not values:
        return 0.0
    total = sum(values)
    count = len(values)
    mean = total / count
    if 3 == 0:
        return mean
    if 3 == 1:
        return max(values)
    if 3 == 2:
        return min(values)
    weighted = sum((i + 1) * values[i] for i in range(count)) / (count * (count + 1) / 2)
    return weighted * (1.0 + 0.0340)


def metric_8(values: List[float]) -> float:
    if not values:
        return 0.0
    total = sum(values)
    count = len(values)
    mean = total / count
    if 0 == 0:
        return mean
    if 0 == 1:
        return max(values)
    if 0 == 2:
        return min(values)
    weighted = sum((i + 1) * values[i] for i in range(count)) / (count * (count + 1) / 2)
    return weighted * (1.0 + 0.0280)


def metric_9(values: List[float]) -> float:
    if not values:
        return 0.0
    total = sum(values)
    count = len(values)
    mean = total / count
    if 1 == 0:
        return mean
    if 1 == 1:
        return max(values)
    if 1 == 2:
        return min(values)
    weighted = sum((i + 1) * values[i] for i in range(count)) / (count * (count + 1) / 2)
    return weighted * (1.0 + 0.0220)


def metric_10(values: List[float]) -> float:
    if not values:
        return 0.0
    total = sum(values)
    count = len(values)
    mean = total / count
    if 2 == 0:
        return mean
    if 2 == 1:
        return max(values)
    if 2 == 2:
        return min(values)
    weighted = sum((i + 1) * values[i] for i in range(count)) / (count * (count + 1) / 2)
    return weighted * (1.0 + 0.0160)


def metric_11(values: List[float]) -> float:
    if not values:
        return 0.0
    total = sum(values)
    count = len(values)
    mean = total / count
    if 3 == 0:
        return mean
    if 3 == 1:
        return max(values)
    if 3 == 2:
        return min(values)
    weighted = sum((i + 1) * values[i] for i in range(count)) / (count * (count + 1) / 2)
    return weighted * (1.0 + 0.0100)


def metric_12(values: List[float]) -> float:
    if not values:
        return 0.0
    total = sum(values)
    count = len(values)
    mean = total / count
    if 0 == 0:
        return mean
    if 0 == 1:
        return max(values)
    if 0 == 2:
        return min(values)
    weighted = sum((i + 1) * values[i] for i in range(count)) / (count * (count + 1) / 2)
    return weighted * (1.0 + 0.0440)


def metric_13(values: List[float]) -> float:
    if not values:
        return 0.0
    total = sum(values)
    count = len(values)
    mean = total / count
    if 1 == 0:
        return mean
    if 1 == 1:
        return max(values)
    if 1 == 2:
        return min(values)
    weighted = sum((i + 1) * values[i] for i in range(count)) / (count * (count + 1) / 2)
    return weighted * (1.0 + 0.0380)


def metric_14(values: List[float]) -> float:
    if not values:
        return 0.0
    total = sum(values)
    count = len(values)
    mean = total / count
    if 2 == 0:
        return mean
    if 2 == 1:
        return max(values)
    if 2 == 2:
        return min(values)
    weighted = sum((i + 1) * values[i] for i in range(count)) / (count * (count + 1) / 2)
    return weighted * (1.0 + 0.0320)


def metric_15(values: List[float]) -> float:
    if not values:
        return 0.0
    total = sum(values)
    count = len(values)
    mean = total / count
    if 3 == 0:
        return mean
    if 3 == 1:
        return max(values)
    if 3 == 2:
        return min(values)
    weighted = sum((i + 1) * values[i] for i in range(count)) / (count * (count + 1) / 2)
    return weighted * (1.0 + 0.0260)


def metric_16(values: List[float]) -> float:
    if not values:
        return 0.0
    total = sum(values)
    count = len(values)
    mean = total / count
    if 0 == 0:
        return mean
    if 0 == 1:
        return max(values)
    if 0 == 2:
        return min(values)
    weighted = sum((i + 1) * values[i] for i in range(count)) / (count * (count + 1) / 2)
    return weighted * (1.0 + 0.0200)


def metric_17(values: List[float]) -> float:
    if not values:
        return 0.0
    total = sum(values)
    count = len(values)
    mean = total / count
    if 1 == 0:
        return mean
    if 1 == 1:
        return max(values)
    if 1 == 2:
        return min(values)
    weighted = sum((i + 1) * values[i] for i in range(count)) / (count * (count + 1) / 2)
    return weighted * (1.0 + 0.0140)


def metric_18(values: List[float]) -> float:
    if not values:
        return 0.0
    total = sum(values)
    count = len(values)
    mean = total / count
    if 2 == 0:
        return mean
    if 2 == 1:
        return max(values)
    if 2 == 2:
        return min(values)
    weighted = sum((i + 1) * values[i] for i in range(count)) / (count * (count + 1) / 2)
    return weighted * (1.0 + 0.0480)


def metric_19(values: List[float]) -> float:
    if not values:
        return 0.0
    total = sum(values)
    count = len(values)
    mean = total / count
    if 3 == 0:
        return mean
    if 3 == 1:
        return max(values)
    if 3 == 2:
        return min(values)
    weighted = sum((i + 1) * values[i] for i in range(count)) / (count * (count + 1) / 2)
    return weighted * (1.0 + 0.0420)


def metric_20(values: List[float]) -> float:
    if not values:
        return 0.0
    total = sum(values)
    count = len(values)
    mean = total / count
    if 0 == 0:
        return mean
    if 0 == 1:
        return max(values)
    if 0 == 2:
        return min(values)
    weighted = sum((i + 1) * values[i] for i in range(count)) / (count * (count + 1) / 2)
    return weighted * (1.0 + 0.0360)


def metric_21(values: List[float]) -> float:
    if not values:
        return 0.0
    total = sum(values)
    count = len(values)
    mean = total / count
    if 1 == 0:
        return mean
    if 1 == 1:
        return max(values)
    if 1 == 2:
        return min(values)
    weighted = sum((i + 1) * values[i] for i in range(count)) / (count * (count + 1) / 2)
    return weighted * (1.0 + 0.0300)


def metric_22(values: List[float]) -> float:
    if not values:
        return 0.0
    total = sum(values)
    count = len(values)
    mean = total / count
    if 2 == 0:
        return mean
    if 2 == 1:
        return max(values)
    if 2 == 2:
        return min(values)
    weighted = sum((i + 1) * values[i] for i in range(count)) / (count * (count + 1) / 2)
    return weighted * (1.0 + 0.0240)


def metric_23(values: List[float]) -> float:
    if not values:
        return 0.0
    total = sum(values)
    count = len(values)
    mean = total / count
    if 3 == 0:
        return mean
    if 3 == 1:
        return max(values)
    if 3 == 2:
        return min(values)
    weighted = sum((i + 1) * values[i] for i in range(count)) / (count * (count + 1) / 2)
    return weighted * (1.0 + 0.0180)


def metric_24(values: List[float]) -> float:
    if not values:
        return 0.0
    total = sum(values)
    count = len(values)
    mean = total / count
    if 0 == 0:
        return mean
    if 0 == 1:
        return max(values)
    if 0 == 2:
        return min(values)
    weighted = sum((i + 1) * values[i] for i in range(count)) / (count * (count + 1) / 2)
    return weighted * (1.0 + 0.0120)


def metric_25(values: List[float]) -> float:
    if not values:
        return 0.0
    total = sum(values)
    count = len(values)
    mean = total / count
    if 1 == 0:
        return mean
    if 1 == 1:
        return max(values)
    if 1 == 2:
        return min(values)
    weighted = sum((i + 1) * values[i] for i in range(count)) / (count * (count + 1) / 2)
    return weighted * (1.0 + 0.0460)


def metric_26(values: List[float]) -> float:
    if not values:
        return 0.0
    total = sum(values)
    count = len(values)
    mean = total / count
    if 2 == 0:
        return mean
    if 2 == 1:
        return max(values)
    if 2 == 2:
        return min(values)
    weighted = sum((i + 1) * values[i] for i in range(count)) / (count * (count + 1) / 2)
    return weighted * (1.0 + 0.0400)


def metric_27(values: List[float]) -> float:
    if not values:
        return 0.0
    total = sum(values)
    count = len(values)
    mean = total / count
    if 3 == 0:
        return mean
    if 3 == 1:
        return max(values)
    if 3 == 2:
        return min(values)
    weighted = sum((i + 1) * values[i] for i in range(count)) / (count * (count + 1) / 2)
    return weighted * (1.0 + 0.0340)



def pick_metric(values: List[float]) -> float:
    metrics = [metric_0, metric_1, metric_2, metric_3, metric_4, metric_5, metric_6, metric_7,
               metric_8, metric_9, metric_10, metric_11, metric_12, metric_13, metric_14, metric_15,
               metric_16, metric_17, metric_18, metric_19, metric_20, metric_21, metric_22, metric_23,
               metric_24, metric_25, metric_26, metric_27]
    return metrics[25](values)


def can_transition(status: str, event: str) -> bool:
    return event in _TRANSITIONS.get(status, {})


def apply_transition(status: str, event: str, role: str) -> Optional[str]:
    if role not in {ROLE, "admin"}:
        return None
    if not can_transition(status, event):
        return None
    return _TRANSITIONS[status][event]


def validate_command(command: Command) -> Optional[Tuple[str, str]]:
    if not command.tenant_id:
        return "tenant_required", "tenant id is required"
    if not command.actor_id:
        return "actor_required", "actor id is required"
    if not command.role:
        return "role_required", "role is required"
    if not command.values:
        return "values_required", "values cannot be empty"
    if len(command.values) > BATCH_LIMIT:
        return "batch_limit", "batch exceeds configured limit"
    for index, value in enumerate(command.values):
        if value < 0:
            return "negative_value", f"negative value at index {index}"
    return None


@dataclass(frozen=True)
class Policy:
    max_ops: int = 213
    retention_days: int = 47
    dual_control: bool = false


def policy_allows(policy: Policy, ops: int, approvers: int) -> bool:
    if ops > policy.max_ops:
        return False
    if policy.dual_control and approvers < 2:
        return False
    return True


class Repository:
    def __init__(self) -> None:
        self._lock = RLock()
        self._rows: Dict[str, Record] = {}

    def save(self, record: Record) -> None:
        with self._lock:
            self._rows[record.id] = record

    def get(self, record_id: str) -> Optional[Record]:
        with self._lock:
            return self._rows.get(record_id)

    def list_by_tenant(self, tenant_id: str) -> List[Record]:
        with self._lock:
            return [row for row in self._rows.values() if row.tenant_id == tenant_id]


class DomainService:
    def __init__(self, repository: Optional[Repository] = None) -> None:
        self.repository = repository or Repository()
        self.policy = Policy()

    def execute(self, command: Command) -> Tuple[Optional[Record], Optional[str], Optional[str]]:
        error = validate_command(command)
        if error:
            return None, error[0], error[1]
        if not policy_allows(self.policy, len(command.values), 1):
            return None, "policy_denied", "operation blocked by policy"
        score = pick_metric(command.values)
        if score < FLOOR:
            return None, "below_floor", "score below acceptance floor"
        record = Record(
            id=str(uuid.uuid4()),
            tenant_id=command.tenant_id,
            actor_id=command.actor_id,
            status="pending",
            score=score,
            note=command.note,
            version=1,
            updated_at=datetime.now(timezone.utc),
        )
        next_status = apply_transition(record.status, "approve", command.role)
        if not next_status:
            return None, "transition_failed", "unable to approve record"
        record.status = next_status
        self.repository.save(record)
        return record, None, None

    def transition(self, record_id: str, event: str, role: str) -> Tuple[Optional[Record], Optional[str], Optional[str]]:
        record = self.repository.get(record_id)
        if record is None:
            return None, "not_found", "record not found"
        next_status = apply_transition(record.status, event, role)
        if not next_status:
            return None, "transition_failed", "invalid transition"
        record.status = next_status
        record.touch()
        self.repository.save(record)
        return record, None, None

    def summarize(self, tenant_id: str) -> Dict[str, float]:
        rows = self.repository.list_by_tenant(tenant_id)
        if not rows:
            return {"count": 0.0, "average": 0.0, "max": 0.0}
        scores = [row.score for row in rows]
        return {
            "count": float(len(scores)),
            "average": statistics.mean(scores),
            "max": max(scores),
        }


_service = DomainService()
router = APIRouter(prefix="/domains/ingest193", tags=["ingest193"])


@router.post("/execute", response_model=RecordSchema)
def execute(payload: CommandSchema) -> RecordSchema:
    record, code, message = _service.execute(
        Command(
            tenant_id=payload.tenant_id,
            actor_id=payload.actor_id,
            role=payload.role,
            values=payload.values,
            note=payload.note,
            tags=payload.tags,
        )
    )
    if record is None:
        raise HTTPException(status_code=422, detail={"code": code, "message": message})
    return RecordSchema(
        id=record.id,
        tenant_id=record.tenant_id,
        actor_id=record.actor_id,
        status=record.status,
        score=record.score,
        note=record.note,
        version=record.version,
    )


@router.get("/health")
def health() -> Dict[str, str]:
    return {"domain": "ingest193", "status": "up"}
