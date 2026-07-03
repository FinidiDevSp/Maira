// Cliente único hacia el backend (docs/technical/API_CONTRACTS.md)
export const API_URL =
  process.env.NEXT_PUBLIC_API_URL ?? "http://localhost:8000";

export type EstadoSalud = "ok" | "arrancando" | "caido";

/** Consulta /health. Render free duerme el backend: "arrancando" no es un error. */
export async function comprobarSalud(): Promise<EstadoSalud> {
  try {
    const respuesta = await fetch(`${API_URL}/health`, { cache: "no-store" });
    if (respuesta.ok) {
      const datos: { status?: string } = await respuesta.json();
      return datos.status === "ok" ? "ok" : "caido";
    }
    return respuesta.status >= 500 ? "arrancando" : "caido";
  } catch {
    return "arrancando";
  }
}
