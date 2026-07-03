"use client";

import Link from "next/link";
import { useState } from "react";
import { useTranslations } from "next-intl";
import { crearClienteNavegador } from "@/lib/supabase/client";

export default function LoginPage() {
  const t = useTranslations("Login");
  const [email, setEmail] = useState("");
  const [estado, setEstado] = useState<"inicial" | "enviando" | "enviado" | "error">("inicial");
  const [errorEmail, setErrorEmail] = useState<string | null>(null);

  async function enviar(evento: React.FormEvent) {
    evento.preventDefault();
    if (!/^[^\s@]+@[^\s@]+\.[^\s@]+$/.test(email)) {
      setErrorEmail(t("emailInvalido"));
      return;
    }
    setErrorEmail(null);
    setEstado("enviando");
    const supabase = crearClienteNavegador();
    const { error } = await supabase.auth.signInWithOtp({
      email,
      options: { emailRedirectTo: `${window.location.origin}/auth/callback` },
    });
    setEstado(error ? "error" : "enviado");
  }

  return (
    <main className="flex min-h-screen flex-col items-center justify-center gap-6 p-8">
      <h1 className="text-3xl font-bold text-primary">{t("titulo")}</h1>
      <p className="max-w-sm text-center">{t("explicacion")}</p>

      <form onSubmit={enviar} className="flex w-full max-w-sm flex-col gap-4" noValidate>
        <div className="flex flex-col gap-1">
          <label htmlFor="email" className="font-medium">
            {t("email")}
          </label>
          <input
            id="email"
            type="email"
            required
            autoComplete="email"
            value={email}
            onChange={(e) => setEmail(e.target.value)}
            aria-invalid={errorEmail != null}
            aria-describedby={errorEmail ? "email-error" : undefined}
            className="rounded-lg border border-muted bg-surface px-4 py-3 focus-visible:outline focus-visible:outline-[3px] focus-visible:outline-primary"
          />
          {errorEmail && (
            <p id="email-error" className="text-sm text-destructive">
              {errorEmail}
            </p>
          )}
        </div>

        <button
          type="submit"
          disabled={estado === "enviando" || estado === "enviado"}
          className="rounded-lg bg-primary px-6 py-3 font-medium text-primary-foreground hover:opacity-90 disabled:opacity-60 focus-visible:outline focus-visible:outline-[3px] focus-visible:outline-offset-2 focus-visible:outline-primary"
        >
          {estado === "enviando" ? t("enviando") : t("enviar")}
        </button>
      </form>

      <p role="status" aria-live="polite" className="max-w-sm text-center">
        {estado === "enviado" && <span className="text-success">{t("enviado")}</span>}
        {estado === "error" && <span className="text-destructive">{t("error")}</span>}
      </p>

      <p className="text-sm text-muted">
        {t("sinCuenta")}{" "}
        <Link href="/signup" className="text-primary underline">
          {t("registrate")}
        </Link>
      </p>
    </main>
  );
}
