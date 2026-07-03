"""Helpers compartidos de tests."""

import uuid
from datetime import UTC, datetime, timedelta

import jwt

SECRETO_TEST = "secreto-jwt-solo-tests-0123456789abcdef"


def crear_token(
    sub: uuid.UUID | str,
    *,
    minutos: int = 60,
    aud: str = "authenticated",
    secreto: str = SECRETO_TEST,
) -> str:
    ahora = datetime.now(UTC)
    return jwt.encode(
        {"sub": str(sub), "aud": aud, "iat": ahora, "exp": ahora + timedelta(minutes=minutos)},
        secreto,
        algorithm="HS256",
    )
