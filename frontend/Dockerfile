FROM node:18-slim AS builder
WORKDIR /app
COPY package.json .
RUN npm install

FROM node:18-slim
WORKDIR /app
COPY --from=builder /app/node_modules ./node_modules
COPY . .
RUN useradd -m appuser
USER appuser
HEALTHCHECK --interval=30s --timeout=10s --start-period=5s --retries=3 \
CMD curl -f http://localhost:3000/health || exit 1
EXPOSE 3000
CMD ["node", "app.js"]
