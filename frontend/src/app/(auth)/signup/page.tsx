"use client";

import Link from "next/link";
import { useState } from "react";
import { useForm } from "react-hook-form";
import { zodResolver } from "@hookform/resolvers/zod";
import { useTranslations } from "next-intl";
import { API_URL } from "@/lib/api";
import { crearSchemaSignup, type SignupFormData } from "@/lib/schemas";

export default function SignupPage() {
  const t = useTranslations("Signup");
  const [estado, setEstado] = useState<"inicial" | "creando" | "creada" | "error">("inicial");
  const [mensajeError, setMensajeError] = useState<string | null>(null);

  const {
    register,
    handleSubmit,
    formState: { errors },
  } = useForm<SignupFormData>({ resolver: zodResolver(crearSchemaSignup(t)) });

  async function crear(datos: SignupFormData) {
    setEstado("creando");
    setMensajeError(null);
    try {
      const respuesta = await fetch(`${API_URL}/api/v1/auth/signup`, {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify(datos),
      });
      if (respuesta.ok) {
        setEstado("creada");
        return;
      }
      const problema: { detail?: string } = await respuesta.json();
      setMensajeError(problema.detail ?? null);
      setEstado("error");
    } catch {
      setEstado("error");
    }
  }

  const claseInput =
    "rounded-lg border border-muted bg-surface px-4 py-3 focus-visible:outline focus-visible:outline-[3px] focus-visible:outline-primary";

  return (
    <main className="flex min-h-screen flex-col items-center justify-center gap-6 p-8">
      <h1 className="text-3xl font-bold text-primary">{t("titulo")}</h1>
      <p className="max-w-sm text-center">{t("explicacion")}</p>

      <form
        onSubmit={handleSubmit(crear)}
        className="flex w-full max-w-sm flex-col gap-4"
        noValidate
      >
        <div className="flex flex-col gap-1">
          <label htmlFor="nombre_protectora" className="font-medium">
            {t("nombreProtectora")}
          </label>
          <input
            id="nombre_protectora"
            {...register("nombre_protectora")}
            aria-invalid={!!errors.nombre_protectora}
            className={claseInput}
          />
          {errors.nombre_protectora && (
            <p className="text-sm text-destructive">{errors.nombre_protectora.message}</p>
          )}
        </div>

        <div className="flex flex-col gap-1">
          <label htmlFor="email" className="font-medium">
            {t("email")}
          </label>
          <input
            id="email"
            type="email"
            autoComplete="email"
            {...register("email")}
            aria-invalid={!!errors.email}
            className={claseInput}
          />
          {errors.email && <p className="text-sm text-destructive">{errors.email.message}</p>}
        </div>

        <div className="flex flex-col gap-1">
          <label htmlFor="persona_responsable" className="font-medium">
            {t("personaResponsable")}
          </label>
          <input id="persona_responsable" {...register("persona_responsable")} className={claseInput} />
        </div>

        <div className="flex flex-col gap-1">
          <label htmlFor="telefono" className="font-medium">
            {t("telefono")}
          </label>
          <input id="telefono" type="tel" {...register("telefono")} className={claseInput} />
        </div>

        <div className="flex items-start gap-2">
          <input
            id="acepta_terminos"
            type="checkbox"
            {...register("acepta_terminos")}
            aria-invalid={!!errors.acepta_terminos}
            className="mt-1 h-5 w-5"
          />
          <label htmlFor="acepta_terminos" className="text-sm">
            {t("terminos")}
          </label>
        </div>
        {errors.acepta_terminos && (
          <p className="text-sm text-destructive">{errors.acepta_terminos.message}</p>
        )}

        <button
          type="submit"
          disabled={estado === "creando" || estado === "creada"}
          className="rounded-lg bg-primary px-6 py-3 font-medium text-primary-foreground hover:opacity-90 disabled:opacity-60 focus-visible:outline focus-visible:outline-[3px] focus-visible:outline-offset-2 focus-visible:outline-primary"
        >
          {estado === "creando" ? t("creando") : t("crear")}
        </button>
      </form>

      <p role="status" aria-live="polite" className="max-w-sm text-center">
        {estado === "creada" && <span className="text-success">{t("creada")}</span>}
        {estado === "error" && mensajeError && (
          <span className="text-destructive">{mensajeError}</span>
        )}
      </p>

      <p className="text-sm text-muted">
        {t("yaTienesCuenta")}{" "}
        <Link href="/login" className="text-primary underline">
          {t("entra")}
        </Link>
      </p>
    </main>
  );
}
