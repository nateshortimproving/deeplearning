import type { PrismaClient } from "@prisma/client";
import type { PantryItem } from "../types/pantry";

export class PantryService {
  constructor(private prisma: PrismaClient) {}

  /**
   * Search pantry items by name (case-insensitive, partial match).
   * PANTRY-005-AC1: Only items matching the search text are returned.
   */
  async searchByName(searchText: string): Promise<PantryItem[]> {
    const trimmed = searchText.trim();
    if (trimmed.length === 0) {
      return [];
    }

    return this.prisma.pantryItem.findMany({
      where: {
        name: {
          contains: trimmed,
          mode: "insensitive",
        },
      },
      orderBy: { name: "asc" },
    });
  }

  /**
   * Filter pantry items by category.
   * PANTRY-005-AC2: Only items in the specified category are returned.
   */
  async filterByCategory(category: string): Promise<PantryItem[]> {
    if (category.trim().length === 0) {
      return [];
    }

    return this.prisma.pantryItem.findMany({
      where: {
        category: {
          equals: category,
          mode: "insensitive",
        },
      },
      orderBy: { name: "asc" },
    });
  }

  /**
   * Search and filter pantry items by name and/or category.
   * Returns items that match both filters (AND logic).
   * If both filters are empty, returns an empty array.
   * PANTRY-005-AC1, AC2, AC3: Supports combined search + category filtering.
   */
  async searchAndFilter(searchText: string, category: string): Promise<PantryItem[]> {
    const searchTrimmed = searchText.trim();
    const categoryTrimmed = category.trim();

    // If both filters are empty, return empty array (no default behavior)
    if (searchTrimmed.length === 0 && categoryTrimmed.length === 0) {
      return [];
    }

    const whereConditions: Record<string, unknown> = {};

    if (searchTrimmed.length > 0) {
      whereConditions.name = {
        contains: searchTrimmed,
        mode: "insensitive",
      };
    }

    if (categoryTrimmed.length > 0) {
      whereConditions.category = {
        equals: categoryTrimmed,
        mode: "insensitive",
      };
    }

    return this.prisma.pantryItem.findMany({
      where: whereConditions,
      orderBy: { name: "asc" },
    });
  }

  /**
   * Get all unique categories in the pantry.
   * Used by the client to populate the category filter dropdown.
   */
  async getAllCategories(): Promise<string[]> {
    const items = await this.prisma.pantryItem.findMany({
      select: { category: true },
      distinct: ["category"],
      orderBy: { category: "asc" },
    });

    return items.map((item) => item.category);
  }
}
