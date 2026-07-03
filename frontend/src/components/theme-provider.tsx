"use client";

import { ThemeProvider as NextThemesProvider } from "next-themes";

// Dark mode según el sistema, con clase en <html> (decisión D-009, DESIGN.md)
export function ThemeProvider({ children }: { children: React.ReactNode }) {
  return (
    <NextThemesProvider attribute="class" defaultTheme="system" enableSystem>
      {children}
    </NextThemesProvider>
  );
}
