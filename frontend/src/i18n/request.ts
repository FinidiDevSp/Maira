import { getRequestConfig } from "next-intl/server";

// MVP: un solo idioma (es-ES). El multi-idioma llega en fase 2 (B-008).
export default getRequestConfig(async () => ({
  locale: "es",
  messages: (await import("../../messages/es.json")).default,
}));
