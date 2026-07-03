"use client";

import { useCallback, useEffect, useState } from "react";
import { comprobarSalud, type EstadoSalud } from "@/lib/api";

const TEXTOS: Record<EstadoSalud | "comprobando", { texto: string; clase: string }> = {
  comprobando: { texto: "Comprobando el servicio…", clase: "text-muted" },
  ok: { texto: "✓ Servicio operativo", clase: "text-success" },
  arrancando: {
    texto: "El servicio está arrancando, puede tardar unos segundos…",
    clase: "text-warning",
  },
  caido: { texto: "El servicio no responde ahora mismo.", clase: "text-destructive" },
};

/** Estado del backend. Render free duerme tras 15 min: "arrancando" reintenta solo. */
export function EstadoBackend() {
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

  const { texto, clase } = TEXTOS[estado];
  return (
    <p role="status" aria-live="polite" className={`text-sm ${clase}`}>
      {texto}
    </p>
  );
}
