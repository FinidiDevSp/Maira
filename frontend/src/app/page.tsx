import { EstadoBackend } from "@/components/estado-backend";

export default function Home() {
  return (
    <main className="flex min-h-screen flex-col items-center justify-center gap-6 p-8">
      <h1 className="text-5xl font-bold tracking-tight text-primary">Maira</h1>
      <p className="max-w-md text-center text-lg">
        Plataforma open source para protectoras de animales pequeñas: fichas de
        adopción con IA, registro diario de salud y triaje veterinario.
      </p>
      <EstadoBackend />
    </main>
  );
}
