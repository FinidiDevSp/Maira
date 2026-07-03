"""Baseline: tablas protectora y usuario (FEATURE-000).

Revision ID: 0001
Revises: None
"""

from collections.abc import Sequence

import sqlalchemy as sa

from alembic import op

revision: str = "0001"
down_revision: str | None = None
branch_labels: str | Sequence[str] | None = None
depends_on: str | Sequence[str] | None = None


def upgrade() -> None:
    op.create_table(
        "protectora",
        sa.Column("id", sa.Uuid(), primary_key=True),
        sa.Column("nombre", sa.String(200), nullable=False),
        sa.Column("email", sa.String(320), nullable=False),
        sa.Column("cif", sa.String(20), nullable=True),
        sa.Column("direccion", sa.String(300), nullable=True),
        sa.Column("telefono", sa.String(20), nullable=True),
        sa.Column("persona_responsable", sa.String(200), nullable=True),
        sa.Column("logo_url", sa.String(500), nullable=True),
        sa.Column("descripcion_publica", sa.Text(), nullable=True),
        sa.Column("created_at", sa.DateTime(), server_default=sa.func.now(), nullable=False),
        sa.Column("updated_at", sa.DateTime(), server_default=sa.func.now(), nullable=False),
    )
    op.create_table(
        "usuario",
        sa.Column("id", sa.Uuid(), primary_key=True),
        sa.Column("protectora_id", sa.Uuid(), sa.ForeignKey("protectora.id"), nullable=False),
        sa.Column("email", sa.String(320), nullable=False, unique=True),
        sa.Column("nombre", sa.String(200), nullable=True),
        sa.Column(
            "rol",
            sa.Enum("admin", "editor", "lectura", name="rolusuario", native_enum=False),
            nullable=False,
        ),
        sa.Column("created_at", sa.DateTime(), server_default=sa.func.now(), nullable=False),
        sa.Column("updated_at", sa.DateTime(), server_default=sa.func.now(), nullable=False),
    )
    op.create_index("ix_usuario_protectora_id", "usuario", ["protectora_id"])


def downgrade() -> None:
    op.drop_index("ix_usuario_protectora_id", table_name="usuario")
    op.drop_table("usuario")
    op.drop_table("protectora")
