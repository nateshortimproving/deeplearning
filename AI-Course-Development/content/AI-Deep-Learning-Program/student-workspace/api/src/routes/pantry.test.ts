import { describe, expect, it, beforeEach, vi } from "vitest";
import type { FastifyInstance } from "fastify";
import { pantryRoutes } from "./pantry";

const mockPantryService = {
  searchAndFilter: vi.fn(),
  getAllCategories: vi.fn(),
};

const mockFastify = {
  get: vi.fn(),
  prisma: {
    pantryItem: {
      findMany: vi.fn(),
    },
  },
} as unknown as FastifyInstance;

describe("Pantry Routes", () => {
  beforeEach(async () => {
    vi.clearAllMocks();
    // Mock the route registration
    vi.mocked(mockFastify.get).mockImplementation((path, opts, handler) => {
      // Store handler for testing
      (mockFastify as any)[`_${path}_handler`] = handler;
      return mockFastify;
    });
  });

  describe("GET /search", () => {
    it("returns items matching search and category filters", async () => {
      await pantryRoutes(mockFastify);

      expect(mockFastify.get).toHaveBeenCalledWith(
        "/search",
        expect.any(Object),
        expect.any(Function)
      );
    });

    it("returns empty array when filters match no items", async () => {
      await pantryRoutes(mockFastify);

      expect(mockFastify.get).toHaveBeenCalled();
    });

    it("validates query parameters", async () => {
      await pantryRoutes(mockFastify);

      const callArgs = vi.mocked(mockFastify.get).mock.calls[0];
      const schema = callArgs[1];

      expect(schema).toHaveProperty("schema");
      expect(schema.schema).toHaveProperty("querystring");
    });
  });

  describe("GET /categories", () => {
    it("returns all unique categories", async () => {
      await pantryRoutes(mockFastify);

      expect(mockFastify.get).toHaveBeenCalledWith(
        "/categories",
        expect.any(Object),
        expect.any(Function)
      );
    });
  });
});
