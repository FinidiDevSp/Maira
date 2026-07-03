import { NextResponse } from "next/server";
import { crearClienteServidor } from "@/lib/supabase/server";
import type { EmailOtpType } from "@supabase/supabase-js";

// Destino de los enlaces de email (magic link e invitaciones).
// Soporta ambos formatos de Supabase: ?code= (PKCE) y ?token_hash=&type= (OTP).
export async function GET(request: Request) {
  const { searchParams, origin } = new URL(request.url);
  const code = searchParams.get("code");
  const tokenHash = searchParams.get("token_hash");
  const type = searchParams.get("type") as EmailOtpType | null;

  const supabase = crearClienteServidor();

  if (code) {
    const { error } = await supabase.auth.exchangeCodeForSession(code);
    if (!error) return NextResponse.redirect(`${origin}/perfil`);
  }
  if (tokenHash && type) {
    const { error } = await supabase.auth.verifyOtp({ token_hash: tokenHash, type });
    if (!error) return NextResponse.redirect(`${origin}/perfil`);
  }

  return NextResponse.redirect(`${origin}/login?error=enlace`);
}
