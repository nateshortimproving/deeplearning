import Fastify from "fastify";
import cors from "@fastify/cors";
import { PrismaClient } from "@prisma/client";
import { pantryRoutes } from "./routes/pantry";

const fastify = Fastify({ logger: true });
const prisma = new PrismaClient();

// Enable CORS
fastify.register(cors, {
  origin: true,
});

// Attach Prisma to Fastify instance
fastify.decorate("prisma", prisma);

// Register routes
fastify.register(async (fastify) => {
  fastify.register(pantryRoutes, { prefix: "/api/pantry" });
});

// Health check endpoint
fastify.get("/health", async (request, reply) => {
  return { status: "ok" };
});

// Start server
const start = async () => {
  try {
    await fastify.listen({ port: 3001, host: "0.0.0.0" });
    console.log("Server running at http://localhost:3001");
  } catch (err) {
    fastify.log.error(err);
    process.exit(1);
  }
};

start();
