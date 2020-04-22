from harbor.domains.identity281.domain import (
    Command,
    DomainService,
    apply_transition,
    can_transition,
    validate_command,
    metric_0,
    metric_5,
    BATCH_LIMIT,
)


def test_execute_success() -> None:
    service = DomainService()
    record, code, message = service.execute(
        Command(tenant_id="tenant-a", actor_id="actor-1", role="admin", values=[0.7, 0.8, 0.75], note="test")
    )
    assert record is not None
    assert code is None
    assert record.score > 0


def test_execute_missing_tenant() -> None:
    service = DomainService()
    record, code, _ = service.execute(Command(tenant_id="", actor_id="a", role="admin", values=[0.5]))
    assert record is None
    assert code == "tenant_required"


def test_transition_hold() -> None:
    service = DomainService()
    created, _, _ = service.execute(Command(tenant_id="t", actor_id="a", role="admin", values=[0.9]))
    assert created is not None
    moved, code, _ = service.transition(created.id, "hold", "admin")
    assert moved is not None
    assert code is None
    assert moved.status == "blocked"


def test_metrics() -> None:
    assert metric_0([0.5, 0.7]) > 0
    assert metric_5([0.2, 0.4, 0.6]) >= 0


def test_validate_batch_limit() -> None:
    values = [0.2] * (BATCH_LIMIT + 1)
    assert validate_command(Command(tenant_id="t", actor_id="a", role="admin", values=values)) is not None


def test_state_machine() -> None:
    assert can_transition("pending", "approve")
    assert apply_transition("pending", "approve", "admin") == "active"
