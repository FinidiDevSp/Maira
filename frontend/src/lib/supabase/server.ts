import { createServerClient } from "@supabase/ssr";
import { cookies } from "next/headers";

// Cliente de Supabase para Server Components y Route Handlers
export function crearClienteServidor() {
  const almacenCookies = cookies();
  return createServerClient(
    process.env.NEXT_PUBLIC_SUPABASE_URL!,
    process.env.NEXT_PUBLIC_SUPABASE_ANON_KEY!,
    {
      cookies: {
        getAll() {
          return almacenCookies.getAll();
        },
        setAll(cookiesASetear) {
          try {
            cookiesASetear.forEach(({ name, value, options }) =>
              almacenCookies.set(name, value, options),
            );
          } catch {
            // Server Component: el middleware se encarga del refresco
          }
        },
      },
    },
  );
}
