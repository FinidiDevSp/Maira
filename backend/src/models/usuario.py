import enum
import uuid

from sqlalchemy import Enum, ForeignKey, String, Uuid
from sqlalchemy.orm import Mapped, mapped_column

from src.models.base import Base, PkUuidMixin, TimestampsMixin


class RolUsuario(enum.Enum):
    """Roles de autorización (docs/operations/SECURITY.md)."""

    ADMIN = "admin"
    EDITOR = "editor"
    LECTURA = "lectura"


class Usuario(Base, PkUuidMixin, TimestampsMixin):
    __tablename__ = "usuario"

    protectora_id: Mapped[uuid.UUID] = mapped_column(Uuid, ForeignKey("protectora.id"), index=True)
    email: Mapped[str] = mapped_column(String(320), unique=True)
    nombre: Mapped[str | None] = mapped_column(String(200))
    rol: Mapped[RolUsuario] = mapped_column(
        Enum(RolUsuario, values_callable=lambda e: [r.value for r in e], native_enum=False),
        default=RolUsuario.LECTURA,
    )
