import { describe, expect, it, beforeEach, vi } from "vitest";
import { PantryService } from "./PantryService";
import type { PrismaClient } from "@prisma/client";

const mockPrisma = {
  pantryItem: {
    findMany: vi.fn(),
  },
} as unknown as PrismaClient;

describe("PantryService", () => {
  let service: PantryService;

  beforeEach(() => {
    service = new PantryService(mockPrisma);
    vi.clearAllMocks();
  });

  describe("searchByName", () => {
    it("returns items matching the search text (case-insensitive)", async () => {
      const mockItems = [
        { id: "1", name: "Milk", quantity: 1, unit: "gallon", category: "Dairy", expirationDate: "2026-10-20" },
      ];
      vi.mocked(mockPrisma.pantryItem.findMany).mockResolvedValue(mockItems);

      const result = await service.searchByName("ilk");

      expect(mockPrisma.pantryItem.findMany).toHaveBeenCalledWith({
        where: {
          name: {
            contains: "ilk",
            mode: "insensitive",
          },
        },
        orderBy: { name: "asc" },
      });
      expect(result).toEqual(mockItems);
    });

    it("returns empty array for empty search text", async () => {
      const result = await service.searchByName("   ");

      expect(mockPrisma.pantryItem.findMany).not.toHaveBeenCalled();
      expect(result).toEqual([]);
    });
  });

  describe("filterByCategory", () => {
    it("returns items in the specified category (case-insensitive)", async () => {
      const mockItems = [
        { id: "1", name: "Milk", quantity: 1, unit: "gallon", category: "Dairy", expirationDate: "2026-10-20" },
      ];
      vi.mocked(mockPrisma.pantryItem.findMany).mockResolvedValue(mockItems);

      const result = await service.filterByCategory("dairy");

      expect(mockPrisma.pantryItem.findMany).toHaveBeenCalledWith({
        where: {
          category: {
            equals: "dairy",
            mode: "insensitive",
          },
        },
        orderBy: { name: "asc" },
      });
      expect(result).toEqual(mockItems);
    });

    it("returns empty array for empty category", async () => {
      const result = await service.filterByCategory("   ");

      expect(mockPrisma.pantryItem.findMany).not.toHaveBeenCalled();
      expect(result).toEqual([]);
    });
  });

  describe("searchAndFilter", () => {
    it("returns items matching both search and category filters", async () => {
      const mockItems = [
        { id: "1", name: "Milk", quantity: 1, unit: "gallon", category: "Dairy", expirationDate: "2026-10-20" },
      ];
      vi.mocked(mockPrisma.pantryItem.findMany).mockResolvedValue(mockItems);

      const result = await service.searchAndFilter("ilk", "Dairy");

      expect(mockPrisma.pantryItem.findMany).toHaveBeenCalledWith({
        where: {
          name: { contains: "ilk", mode: "insensitive" },
          category: { equals: "Dairy", mode: "insensitive" },
        },
        orderBy: { name: "asc" },
      });
      expect(result).toEqual(mockItems);
    });

    it("returns empty array when both filters are empty", async () => {
      const result = await service.searchAndFilter("", "");

      expect(mockPrisma.pantryItem.findMany).not.toHaveBeenCalled();
      expect(result).toEqual([]);
    });

    it("returns empty array when filters match no items", async () => {
      vi.mocked(mockPrisma.pantryItem.findMany).mockResolvedValue([]);

      const result = await service.searchAndFilter("Milk", "Produce");

      expect(result).toEqual([]);
    });
  });

  describe("getAllCategories", () => {
    it("returns a sorted list of unique categories", async () => {
      const mockItems = [
        { category: "Dairy" },
        { category: "Produce" },
        { category: "Grains" },
      ];
      vi.mocked(mockPrisma.pantryItem.findMany).mockResolvedValue(mockItems);

      const result = await service.getAllCategories();

      expect(mockPrisma.pantryItem.findMany).toHaveBeenCalledWith({
        select: { category: true },
        distinct: ["category"],
        orderBy: { category: "asc" },
      });
      expect(result).toEqual(["Dairy", "Produce", "Grains"]);
    });
  });
});
