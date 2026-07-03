"use client";

import { useRouter } from "next/navigation";
import { crearClienteNavegador } from "@/lib/supabase/client";

export function BotonSalir({ etiqueta }: { etiqueta: string }) {
  const router = useRouter();

  async function salir() {
    await crearClienteNavegador().auth.signOut();
    router.push("/");
    router.refresh();
  }

  return (
    <button
      onClick={salir}
      className="rounded-lg border border-muted px-4 py-2 text-sm hover:bg-muted/10 focus-visible:outline focus-visible:outline-[3px] focus-visible:outline-primary"
    >
      {etiqueta}
    </button>
  );
}
