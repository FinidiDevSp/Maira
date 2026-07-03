import Link from "next/link";
import { getTranslations } from "next-intl/server";
import { EstadoBackend } from "@/components/estado-backend";

export default async function Home() {
  const t = await getTranslations("Home");
  return (
    <main className="flex min-h-screen flex-col items-center justify-center gap-6 p-8">
      <h1 className="text-5xl font-bold tracking-tight text-primary">{t("titulo")}</h1>
      <p className="max-w-md text-center text-lg">{t("descripcion")}</p>
      <div className="flex gap-4">
        <Link
          href="/login"
          className="rounded-lg bg-primary px-6 py-3 font-medium text-primary-foreground hover:opacity-90 focus-visible:outline focus-visible:outline-[3px] focus-visible:outline-offset-2 focus-visible:outline-primary"
        >
          {t("entrar")}
        </Link>
        <Link
          href="/signup"
          className="rounded-lg border-2 border-primary px-6 py-3 font-medium text-primary hover:bg-primary/10 focus-visible:outline focus-visible:outline-[3px] focus-visible:outline-offset-2 focus-visible:outline-primary"
        >
          {t("registrarProtectora")}
        </Link>
      </div>
      <EstadoBackend />
    </main>
  );
}
