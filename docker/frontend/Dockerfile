# Frontend Maira (Next.js 14) — multi-stage.
# development: next dev con volumen montado.
# production: build standalone sin root (el deploy real es Vercel; esto es el plan B local).

FROM node:20-alpine AS base
WORKDIR /app

# --- development ---
FROM base AS development
COPY frontend/package*.json ./
RUN npm install
COPY frontend/ ./
EXPOSE 3000
CMD ["npm", "run", "dev"]

# --- production ---
FROM base AS builder
COPY frontend/package*.json ./
RUN npm ci
COPY frontend/ ./
RUN npm run build

FROM base AS production
RUN addgroup -S maira && adduser -S maira -G maira
COPY --from=builder --chown=maira:maira /app/.next/standalone ./
COPY --from=builder --chown=maira:maira /app/.next/static ./.next/static
COPY --from=builder --chown=maira:maira /app/public ./public
USER maira
EXPOSE 3000
CMD ["node", "server.js"]
