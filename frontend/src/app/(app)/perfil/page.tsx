import { redirect } from "next/navigation";
import { getTranslations } from "next-intl/server";
import { API_URL } from "@/lib/api";
import { crearClienteServidor } from "@/lib/supabase/server";
import { BotonSalir } from "./boton-salir";
import { InvitarForm } from "./invitar-form";

type Protectora = {
  nombre: string;
  email: string;
  telefono: string | null;
  persona_responsable: string | null;
  descripcion_publica: string | null;
};

type Voluntaria = { id: string; email: string; nombre: string | null; rol: string };

export default async function PerfilPage() {
  const t = await getTranslations("Perfil");
  const supabase = crearClienteServidor();
  const {
    data: { session },
  } = await supabase.auth.getSession();
  if (!session) redirect("/login");

  const cabeceras = { Authorization: `Bearer ${session.access_token}` };
  const [rProtectora, rVoluntarias] = await Promise.all([
    fetch(`${API_URL}/api/v1/protectora/me`, { headers: cabeceras, cache: "no-store" }),
    fetch(`${API_URL}/api/v1/protectora/usuarios`, { headers: cabeceras, cache: "no-store" }),
  ]);
  if (!rProtectora.ok) redirect("/login");

  const protectora: Protectora = await rProtectora.json();
  const voluntarias: Voluntaria[] = rVoluntarias.ok ? await rVoluntarias.json() : [];
  const roles = { admin: t("roles.admin"), editor: t("roles.editor"), lectura: t("roles.lectura") };
  // El backend ya lo bloquea (requiere_rol); esto evita mostrar un formulario que fallaría
  const soyAdmin =
    voluntarias.find((v) => v.email === session.user.email)?.rol === "admin";

  return (
    <main className="mx-auto flex min-h-screen max-w-2xl flex-col gap-8 p-8">
      <header className="flex items-center justify-between">
        <h1 className="text-3xl font-bold text-primary">{protectora.nombre}</h1>
        <BotonSalir etiqueta={t("salir")} />
      </header>

      <section className="rounded-xl bg-surface p-6 shadow-sm">
        <h2 className="mb-3 text-xl font-semibold">{t("titulo")}</h2>
        <dl className="grid gap-2">
          <div>
            <dt className="text-sm text-muted">Email</dt>
            <dd>{protectora.email}</dd>
          </div>
          {protectora.persona_responsable && (
            <div>
              <dt className="text-sm text-muted">{t("roles.admin")}</dt>
              <dd>{protectora.persona_responsable}</dd>
            </div>
          )}
          {protectora.descripcion_publica && <dd>{protectora.descripcion_publica}</dd>}
        </dl>
      </section>

      <section className="rounded-xl bg-surface p-6 shadow-sm">
        <h2 className="mb-3 text-xl font-semibold">{t("voluntarias")}</h2>
        <ul className="flex flex-col gap-2">
          {voluntarias.map((v) => (
            <li key={v.id} className="flex items-center justify-between border-b border-muted/30 pb-2">
              <span>{v.nombre ?? v.email}</span>
              <span className="text-sm text-muted">
                {roles[v.rol as keyof typeof roles] ?? v.rol}
              </span>
            </li>
          ))}
        </ul>
        {soyAdmin && <InvitarForm token={session.access_token} />}
      </section>
    </main>
  );
}
