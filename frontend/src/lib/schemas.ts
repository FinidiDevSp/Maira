import { z } from "zod";

type Traductor = (clave: string) => string;

// Factoría: los mensajes de error salen de messages/es.json (nada hardcodeado)
export function crearSchemaSignup(t: Traductor) {
  return z.object({
    nombre_protectora: z.string().trim().min(2, t("nombreCorto")).max(200),
    email: z.string().trim().email(t("emailInvalido")),
    persona_responsable: z.string().trim().max(200).optional(),
    telefono: z.string().trim().max(20).optional(),
    acepta_terminos: z.literal(true, { message: t("aceptaTerminos") }),
  });
}

export type SignupFormData = z.infer<ReturnType<typeof crearSchemaSignup>>;
