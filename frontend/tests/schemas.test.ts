/** FEATURE-001: validación del formulario de registro de protectora. */
import { describe, expect, it } from "vitest";
import { crearSchemaSignup } from "@/lib/schemas";

const t = (clave: string) => clave; // los mensajes reales viven en messages/es.json

const schema = crearSchemaSignup(t);

const DATOS_OK = {
  nombre_protectora: "Refugio Esperanza",
  email: "lucia@refugio.example",
  acepta_terminos: true as const,
};

describe("schema de signup", () => {
  it("acepta datos válidos mínimos", () => {
    expect(schema.safeParse(DATOS_OK).success).toBe(true);
  });

  it("rechaza nombre de protectora demasiado corto", () => {
    const resultado = schema.safeParse({ ...DATOS_OK, nombre_protectora: "A" });
    expect(resultado.success).toBe(false);
  });

  it("rechaza email inválido", () => {
    const resultado = schema.safeParse({ ...DATOS_OK, email: "no-es-un-email" });
    expect(resultado.success).toBe(false);
  });

  it("rechaza si no se aceptan los términos", () => {
    const resultado = schema.safeParse({ ...DATOS_OK, acepta_terminos: false });
    expect(resultado.success).toBe(false);
  });

  it("recorta espacios en los campos de texto", () => {
    const resultado = schema.parse({ ...DATOS_OK, nombre_protectora: "  Refugio  " });
    expect(resultado.nombre_protectora).toBe("Refugio");
  });
});
