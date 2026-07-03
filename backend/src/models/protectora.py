from sqlalchemy import String, Text
from sqlalchemy.orm import Mapped, mapped_column

from src.models.base import Base, PkUuidMixin, TimestampsMixin


class Protectora(Base, PkUuidMixin, TimestampsMixin):
    __tablename__ = "protectora"

    nombre: Mapped[str] = mapped_column(String(200))
    email: Mapped[str] = mapped_column(String(320))
    cif: Mapped[str | None] = mapped_column(String(20))
    direccion: Mapped[str | None] = mapped_column(String(300))
    telefono: Mapped[str | None] = mapped_column(String(20))
    persona_responsable: Mapped[str | None] = mapped_column(String(200))
    logo_url: Mapped[str | None] = mapped_column(String(500))
    descripcion_publica: Mapped[str | None] = mapped_column(Text)
