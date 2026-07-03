"use client";

import { useEffect, useRef, useState } from "react";
import Link from "next/link";
import { useRouter } from "next/navigation";
import { useTranslations } from "next-intl";
import type { EmailOtpType } from "@supabase/supabase-js";
import { crearClienteNavegador } from "@/lib/supabase/client";

/**
 * Destino de los enlaces de email de Supabase. Soporta los tres formatos:
 * ?code= (PKCE, magic link iniciado en el navegador), ?token_hash=&type=
 * (plantillas personalizadas) y #access_token= (flujo implícito: invitaciones
 * creadas por el backend). El fragmento # solo existe en el navegador, por eso
 * esta página es de cliente y no un route handler.
 */
export default function CallbackPage() {
  const t = useTranslations("Callback");
  const router = useRouter();
  const [fallo, setFallo] = useState(false);
  const procesado = useRef(false);

  useEffect(() => {
    if (procesado.current) return;
    procesado.current = true;

    async function procesar() {
      const supabase = crearClienteNavegador();
      const url = new URL(window.location.href);
      const code = url.searchParams.get("code");
      const tokenHash = url.searchParams.get("token_hash");
      const type = url.searchParams.get("type") as EmailOtpType | null;
      const hash = new URLSearchParams(window.location.hash.slice(1));
      const accessToken = hash.get("access_token");
      const refreshToken = hash.get("refresh_token");

      let ok = false;
      if (code) {
        ok = !(await supabase.auth.exchangeCodeForSession(code)).error;
      } else if (tokenHash && type) {
        ok = !(await supabase.auth.verifyOtp({ token_hash: tokenHash, type })).error;
      } else if (accessToken && refreshToken) {
        ok = !(
          await supabase.auth.setSession({
            access_token: accessToken,
            refresh_token: refreshToken,
          })
        ).error;
      }

      if (ok) {
        router.replace("/perfil");
        router.refresh();
      } else {
        setFallo(true);
      }
    }
    void procesar();
  }, [router]);

  return (
    <main className="flex min-h-screen flex-col items-center justify-center gap-4 p-8">
      <p role="status" aria-live="polite" className={fallo ? "text-destructive" : "text-muted"}>
        {fallo ? t("error") : t("procesando")}
      </p>
      {fallo && (
        <Link href="/login" className="text-primary underline">
          {t("volverLogin")}
        </Link>
      )}
    </main>
  );
}
