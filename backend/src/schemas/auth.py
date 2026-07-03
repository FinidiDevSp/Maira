import uuid

from pydantic import BaseModel, EmailStr, Field, field_validator


class SignupRequest(BaseModel):
    email: EmailStr
    nombre_protectora: str = Field(min_length=2, max_length=200)
    cif: str | None = Field(default=None, max_length=20)
    direccion: str | None = Field(default=None, max_length=300)
    telefono: str | None = Field(default=None, max_length=20)
    persona_responsable: str | None = Field(default=None, max_length=200)
    acepta_terminos: bool

    @field_validator("acepta_terminos")
    @classmethod
    def debe_aceptar(cls, valor: bool) -> bool:
        if not valor:
            raise ValueError("Debes aceptar los términos de uso y la política de privacidad.")
        return valor


class SignupResponse(BaseModel):
    protectora_id: uuid.UUID
    usuario_id: uuid.UUID
    mensaje: str
