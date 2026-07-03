"""RLS en protectora y usuario (FEATURE-001, defensa en profundidad).

El backend (owner) no está sujeto a RLS: la autorización primaria vive en
FastAPI. Estas políticas protegen ante acceso directo con el rol
`authenticated` de Supabase (PostgREST, supabase-js, etc.).

Revision ID: 0002
Revises: 0001
"""

from collections.abc import Sequence

from alembic import op

revision: str = "0002"
down_revision: str | None = "0001"
branch_labels: str | Sequence[str] | None = None
depends_on: str | Sequence[str] | None = None

# En Supabase auth.uid() ya existe; en el Postgres local de Docker se crea un
# stub equivalente (lee el claim sub) para que la migración sea idéntica.
# Nota: una sentencia por op.execute — asyncpg no acepta lotes multi-sentencia.
CREAR_SCHEMA_AUTH = "CREATE SCHEMA IF NOT EXISTS auth"

STUB_AUTH_UID = """
DO $$
BEGIN
    IF NOT EXISTS (
        SELECT 1 FROM pg_proc p
        JOIN pg_namespace n ON p.pronamespace = n.oid
        WHERE n.nspname = 'auth' AND p.proname = 'uid'
    ) THEN
        CREATE FUNCTION auth.uid() RETURNS uuid
        LANGUAGE sql STABLE
        AS 'SELECT nullif(current_setting(''request.jwt.claim.sub'', true), '''')::uuid';
    END IF;
END
$$;
"""

# SECURITY DEFINER evita la recursión de una política de usuario que consulta usuario
FUNCION_MI_PROTECTORA = """
CREATE OR REPLACE FUNCTION public.mi_protectora_id() RETURNS uuid
LANGUAGE sql STABLE SECURITY DEFINER SET search_path = public
AS 'SELECT protectora_id FROM usuario WHERE id = auth.uid()';
"""


def upgrade() -> None:
    op.execute(CREAR_SCHEMA_AUTH)
    op.execute(STUB_AUTH_UID)
    op.execute(FUNCION_MI_PROTECTORA)
    op.execute("ALTER TABLE protectora ENABLE ROW LEVEL SECURITY")
    op.execute("ALTER TABLE usuario ENABLE ROW LEVEL SECURITY")
    op.execute(
        "CREATE POLICY tenant_protectora ON protectora FOR ALL "
        "USING (id = public.mi_protectora_id())"
    )
    op.execute(
        "CREATE POLICY tenant_usuario ON usuario FOR ALL "
        "USING (protectora_id = public.mi_protectora_id())"
    )


def downgrade() -> None:
    op.execute("DROP POLICY IF EXISTS tenant_usuario ON usuario")
    op.execute("DROP POLICY IF EXISTS tenant_protectora ON protectora")
    op.execute("ALTER TABLE usuario DISABLE ROW LEVEL SECURITY")
    op.execute("ALTER TABLE protectora DISABLE ROW LEVEL SECURITY")
    op.execute("DROP FUNCTION IF EXISTS public.mi_protectora_id()")
    # El stub auth.uid() se conserva: es inocuo y en Supabase no es nuestro
