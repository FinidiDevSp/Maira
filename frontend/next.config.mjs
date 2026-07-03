/** @type {import('next').NextConfig} */
const nextConfig = {
  // standalone: necesario para la imagen Docker de producción (plan B de demo)
  output: "standalone",
};

export default nextConfig;
