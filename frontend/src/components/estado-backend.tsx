"use client";

import { useCallback, useEffect, useState } from "react";
import { useTranslations } from "next-intl";
import { comprobarSalud, type EstadoSalud } from "@/lib/api";

const CLASES: Record<EstadoSalud | "comprobando", string> = {
  comprobando: "text-muted",
  ok: "text-success",
  arrancando: "text-warning",
  caido: "text-destructive",
};

/** Estado del backend. Render free duerme tras 15 min: "arrancando" reintenta solo. */
export function EstadoBackend() {
  const t = useTranslations("EstadoBackend");
  const [estado, setEstado] = useState<EstadoSalud | "comprobando">("comprobando");

  const comprobar = useCallback(async () => {
    setEstado(await comprobarSalud());
  }, []);

  useEffect(() => {
    void comprobar();
  }, [comprobar]);

  useEffect(() => {
    if (estado !== "arrancando") return;
    const temporizador = setTimeout(() => void comprobar(), 5000);
    return () => clearTimeout(temporizador);
  }, [estado, comprobar]);

  return (
    <p role="status" aria-live="polite" className={`text-sm ${CLASES[estado]}`}>
      {t(estado)}
    </p>
  );
}
