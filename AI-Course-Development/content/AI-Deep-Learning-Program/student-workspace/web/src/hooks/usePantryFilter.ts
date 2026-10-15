import { useMemo, useState, useEffect } from "react";
import type { PantryItem } from "../types/pantry";

export interface PantryFilters {
  search: string;
  category: string;
}

/**
 * Hook for searching and filtering pantry items via the API.
 * PANTRY-005-AC1, AC2, AC3: Calls /api/pantry/search with search and category params.
 */
export function usePantryFilter() {
  const [filters, setFilters] = useState<PantryFilters>({ search: "", category: "" });
  const [items, setItems] = useState<PantryItem[]>([]);
  const [categories, setCategories] = useState<string[]>([]);
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState<string | null>(null);

  // Fetch categories on mount
  useEffect(() => {
    const fetchCategories = async () => {
      try {
        const response = await fetch("/api/pantry/categories");
        if (!response.ok) throw new Error("Failed to fetch categories");
        const data = await response.json();
        setCategories(data.categories);
      } catch (err) {
        setError(err instanceof Error ? err.message : "Unknown error");
      }
    };

    fetchCategories();
  }, []);

  // Fetch items when filters change
  useEffect(() => {
    const fetchItems = async () => {
      setLoading(true);
      setError(null);

      try {
        const params = new URLSearchParams();
        if (filters.search) params.append("search", filters.search);
        if (filters.category) params.append("category", filters.category);

        const response = await fetch(`/api/pantry/search?${params.toString()}`);
        if (!response.ok) throw new Error("Failed to fetch items");

        const data = await response.json();
        setItems(data.items);
      } catch (err) {
        setError(err instanceof Error ? err.message : "Unknown error");
        setItems([]);
      } finally {
        setLoading(false);
      }
    };

    fetchItems();
  }, [filters]);

  const clearFilters = () => setFilters({ search: "", category: "" });

  return {
    filters,
    setFilters,
    clearFilters,
    items,
    categories,
    loading,
    error,
    hasActiveFilters: filters.search.length > 0 || filters.category.length > 0,
  };
}
