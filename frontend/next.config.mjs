import createNextIntlPlugin from "next-intl/plugin";

const withNextIntl = createNextIntlPlugin("./src/i18n/request.ts");

/** @type {import('next').NextConfig} */
const nextConfig = {
  // standalone: necesario para la imagen Docker de producción (plan B de demo)
  output: "standalone",
};

export default withNextIntl(nextConfig);
