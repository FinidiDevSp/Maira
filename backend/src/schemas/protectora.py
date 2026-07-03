import uuid

from pydantic import BaseModel, ConfigDict, EmailStr, Field

from src.models import RolUsuario


class ProtectoraOut(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    id: uuid.UUID
    nombre: str
    email: str
    cif: str | None
    direccion: str | None
    telefono: str | None
    persona_responsable: str | None
    logo_url: str | None
    descripcion_publica: str | None


class ProtectoraUpdate(BaseModel):
    nombre: str | None = Field(default=None, min_length=2, max_length=200)
    cif: str | None = Field(default=None, max_length=20)
    direccion: str | None = Field(default=None, max_length=300)
    telefono: str | None = Field(default=None, max_length=20)
    persona_responsable: str | None = Field(default=None, max_length=200)
    logo_url: str | None = Field(default=None, max_length=500)
    descripcion_publica: str | None = Field(default=None, max_length=2000)


class UsuarioOut(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    id: uuid.UUID
    email: str
    nombre: str | None
    rol: RolUsuario


class InvitacionRequest(BaseModel):
    email: EmailStr
    rol: RolUsuario


class InvitacionResponse(BaseModel):
    usuario_id: uuid.UUID
    mensaje: str
