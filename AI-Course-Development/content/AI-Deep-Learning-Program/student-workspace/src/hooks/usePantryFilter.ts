import { useMemo, useState } from "react";
import type { PantryItem } from "../types/pantry";

export interface PantryFilters {
  search: string;
  category: string;
}

export function usePantryFilter(items: PantryItem[], categories: string[]) {
  const [filters, setFilters] = useState<PantryFilters>({ search: "", category: "" });

  const filteredItems = useMemo(() => {
    const searchLower = filters.search.trim().toLowerCase();

    return items.filter((item) => {
      const matchesSearch = searchLower.length === 0 || item.name.toLowerCase().includes(searchLower);
      const matchesCategory = filters.category.length === 0 || item.category === filters.category;
      return matchesSearch && matchesCategory;
    });
  }, [items, filters]);

  const clearFilters = () => setFilters({ search: "", category: "" });

  return {
    filters,
    setFilters,
    clearFilters,
    filteredItems,
    categories,
    hasActiveFilters: filters.search.length > 0 || filters.category.length > 0,
  };
}
