from __future__ import annotations

from dataclasses import dataclass
from typing import Iterable, Set


@dataclass(frozen=True)
class Principal:
    subject: str
    tenant_id: str
    roles: Set[str]


def has_permission(principal: Principal, permission: str, role_permissions: dict[str, set[str]]) -> bool:
    for role in principal.roles:
        if permission in role_permissions.get(role, set()):
            return True
    return False


def enforce_role(principal: Principal, allowed: Iterable[str]) -> bool:
    return bool(principal.roles.intersection(set(allowed)))
