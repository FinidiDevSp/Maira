"""Logging estructurado JSON con structlog (se recoge desde stdout en Render)."""

import logging

import structlog


def configurar_logging(environment: str) -> None:
    nivel = logging.DEBUG if environment == "development" else logging.INFO
    logging.basicConfig(level=nivel, format="%(message)s")
    structlog.configure(
        processors=[
            structlog.contextvars.merge_contextvars,
            structlog.processors.add_log_level,
            structlog.processors.TimeStamper(fmt="iso", utc=True),
            structlog.processors.JSONRenderer(ensure_ascii=False),
        ],
        wrapper_class=structlog.make_filtering_bound_logger(nivel),
    )
