import type { FastifyInstance } from "fastify";
import { Type } from "@sinclair/typebox";
import { PantryService } from "../services/PantryService";
import type { SearchAndFilterResponse } from "../types/pantry";

export async function pantryRoutes(fastify: FastifyInstance) {
  const pantryService = new PantryService(fastify.prisma);

  // GET /api/pantry/search?search=...&category=...
  // PANTRY-005-AC1, AC2, AC3: Search and filter pantry items
  fastify.get<{
    Querystring: {
      search?: string;
      category?: string;
    };
    Reply: SearchAndFilterResponse;
  }>(
    "/search",
    {
      schema: {
        querystring: Type.Object({
          search: Type.Optional(Type.String({ minLength: 0, maxLength: 100 })),
          category: Type.Optional(Type.String({ minLength: 0, maxLength: 100 })),
        }),
        response: {
          200: Type.Object({
            items: Type.Array(
              Type.Object({
                id: Type.String(),
                name: Type.String(),
                quantity: Type.Number(),
                unit: Type.String(),
                category: Type.String(),
                expirationDate: Type.String(),
              })
            ),
            count: Type.Number(),
          }),
        },
      },
    },
    async (request, reply) => {
      const searchText = request.query.search ?? "";
      const category = request.query.category ?? "";

      const items = await pantryService.searchAndFilter(searchText, category);

      return reply.send({
        items,
        count: items.length,
      });
    }
  );

  // GET /api/pantry/categories
  // Returns all unique categories for the filter dropdown
  fastify.get<{
    Reply: { categories: string[] };
  }>(
    "/categories",
    {
      schema: {
        response: {
          200: Type.Object({
            categories: Type.Array(Type.String()),
          }),
        },
      },
    },
    async (request, reply) => {
      const categories = await pantryService.getAllCategories();

      return reply.send({ categories });
    }
  );
}
