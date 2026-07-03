/** FEATURE-000 · Tarea TDD 5: la home informa del estado del backend, incluido el cold start. */
import { render, screen, waitFor } from "@testing-library/react";
import { afterEach, describe, expect, it, vi } from "vitest";
import { EstadoBackend } from "@/components/estado-backend";

afterEach(() => {
  vi.unstubAllGlobals();
  vi.restoreAllMocks();
});

describe("EstadoBackend", () => {
  it("muestra 'operativo' cuando /health responde ok", async () => {
    vi.stubGlobal(
      "fetch",
      vi.fn().mockResolvedValue(
        new Response(JSON.stringify({ status: "ok" }), { status: 200 }),
      ),
    );
    render(<EstadoBackend />);
    await waitFor(() =>
      expect(screen.getByRole("status")).toHaveTextContent("Servicio operativo"),
    );
  });

  it("muestra 'arrancando' cuando el backend no contesta (Render dormido)", async () => {
    vi.stubGlobal("fetch", vi.fn().mockRejectedValue(new TypeError("fetch failed")));
    render(<EstadoBackend />);
    await waitFor(() =>
      expect(screen.getByRole("status")).toHaveTextContent("arrancando"),
    );
  });

  it("muestra 'no responde' ante un error 4xx", async () => {
    vi.stubGlobal(
      "fetch",
      vi.fn().mockResolvedValue(new Response("no", { status: 404 })),
    );
    render(<EstadoBackend />);
    await waitFor(() =>
      expect(screen.getByRole("status")).toHaveTextContent("no responde"),
    );
  });
});
