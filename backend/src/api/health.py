"""Endpoint de salud: lo consultan Render, Healthchecks.io y la home del frontend."""

from fastapi import APIRouter

router = APIRouter(tags=["salud"])


@router.get("/health")
async def health() -> dict[str, str]:
    return {"status": "ok"}
