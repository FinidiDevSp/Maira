"""FEATURE-000 · Tarea TDD 2: la configuración lee de env y falla claro si falta algo."""

import pytest
from pydantic import ValidationError


def test_settings_lee_variables_de_entorno() -> None:
    from src.config import get_settings

    settings = get_settings()
    assert settings.environment == "development"
    assert settings.database_url.startswith("sqlite+aiosqlite")


def test_cors_origins_se_parsea_como_lista() -> None:
    from src.config import get_settings

    settings = get_settings()
    assert settings.cors_origins_list == ["http://localhost:3000"]


def test_falta_secret_key_falla_al_arrancar(monkeypatch: pytest.MonkeyPatch) -> None:
    from src.config import Settings

    monkeypatch.delenv("SECRET_KEY", raising=False)
    with pytest.raises(ValidationError):
        Settings(_env_file=None)  # type: ignore[call-arg]
