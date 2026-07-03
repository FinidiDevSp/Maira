"use client";

import { useState } from "react";
import { useRouter } from "next/navigation";
import { useTranslations } from "next-intl";
import { API_URL } from "@/lib/api";

export function InvitarForm({ token }: { token: string }) {
  const t = useTranslations("Perfil");
  const router = useRouter();
  const [email, setEmail] = useState("");
  const [rol, setRol] = useState("editor");
  const [estado, setEstado] = useState<"inicial" | "enviando" | "invitada" | "error">("inicial");
  const [mensajeError, setMensajeError] = useState<string | null>(null);

  async function invitar(evento: React.FormEvent) {
    evento.preventDefault();
    setEstado("enviando");
    setMensajeError(null);
    try {
      const respuesta = await fetch(`${API_URL}/api/v1/protectora/usuarios`, {
        method: "POST",
        headers: { "Content-Type": "application/json", Authorization: `Bearer ${token}` },
        body: JSON.stringify({ email, rol }),
      });
      if (respuesta.ok) {
        setEstado("invitada");
        setEmail("");
        router.refresh();
        return;
      }
      const problema: { detail?: string } = await respuesta.json();
      setMensajeError(problema.detail ?? t("errorInvitar"));
      setEstado("error");
    } catch {
      setMensajeError(t("errorInvitar"));
      setEstado("error");
    }
  }

  return (
    <form onSubmit={invitar} className="mt-4 flex flex-col gap-3 border-t border-muted/30 pt-4">
      <h3 className="font-medium">{t("invitar")}</h3>
      <div className="flex flex-col gap-1">
        <label htmlFor="email-invitacion" className="text-sm">
          {t("emailVoluntaria")}
        </label>
        <input
          id="email-invitacion"
          type="email"
          required
          value={email}
          onChange={(e) => setEmail(e.target.value)}
          className="rounded-lg border border-muted bg-background px-3 py-2 focus-visible:outline focus-visible:outline-[3px] focus-visible:outline-primary"
        />
      </div>
      <div className="flex flex-col gap-1">
        <label htmlFor="rol-invitacion" className="text-sm">
          {t("rolInvitacion")}
        </label>
        <select
          id="rol-invitacion"
          value={rol}
          onChange={(e) => setRol(e.target.value)}
          className="rounded-lg border border-muted bg-background px-3 py-2 focus-visible:outline focus-visible:outline-[3px] focus-visible:outline-primary"
        >
          <option value="editor">{t("roles.editor")}</option>
          <option value="lectura">{t("roles.lectura")}</option>
          <option value="admin">{t("roles.admin")}</option>
        </select>
      </div>
      <button
        type="submit"
        disabled={estado === "enviando"}
        className="rounded-lg bg-primary px-4 py-2 font-medium text-primary-foreground hover:opacity-90 disabled:opacity-60 focus-visible:outline focus-visible:outline-[3px] focus-visible:outline-offset-2 focus-visible:outline-primary"
      >
        {estado === "enviando" ? t("enviando") : t("enviarInvitacion")}
      </button>
      <p role="status" aria-live="polite" className="text-sm">
        {estado === "invitada" && <span className="text-success">{t("invitada")}</span>}
        {estado === "error" && mensajeError && (
          <span className="text-destructive">{mensajeError}</span>
        )}
      </p>
    </form>
  );
}
