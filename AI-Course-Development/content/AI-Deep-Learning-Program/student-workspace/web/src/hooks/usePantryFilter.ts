import { useState, useEffect, useCallback, useRef } from "react";
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
  const [filters, setFiltersState] = useState<PantryFilters>({ search: "", category: "" });
  const [debouncedFilters, setDebouncedFilters] = useState<PantryFilters>({ search: "", category: "" });
  const [items, setItems] = useState<PantryItem[]>([]);
  const [categories, setCategories] = useState<string[]>([]);
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState<string | null>(null);
  const debounceTimer = useRef<NodeJS.Timeout | null>(null);

  const setFilters = useCallback((updater: PantryFilters | ((prev: PantryFilters) => PantryFilters)) => {
    setFiltersState((prev) => {
      const newFilters = typeof updater === "function" ? updater(prev) : updater;
      return newFilters;
    });
  }, []);

  // Fetch categories on mount
  useEffect(() => {
    const fetchCategories = async () => {
      try {
        const response = await fetch("http://localhost:3001/api/pantry/categories");
        if (!response.ok) throw new Error("Failed to fetch categories");
        const data = await response.json();
        setCategories(data.categories);
      } catch (err) {
        setError(err instanceof Error ? err.message : "Unknown error");
      }
    };

    fetchCategories();
  }, []);

  // Debounce filter changes
  useEffect(() => {
    if (debounceTimer.current) {
      clearTimeout(debounceTimer.current);
    }

    debounceTimer.current = setTimeout(() => {
      setDebouncedFilters(filters);
    }, 300);

    return () => {
      if (debounceTimer.current) {
        clearTimeout(debounceTimer.current);
      }
    };
  }, [filters]);

  // Fetch items when debounced filters change
  useEffect(() => {
    const fetchItems = async () => {
      setLoading(true);
      setError(null);

      try {
        const params = new URLSearchParams();
        if (debouncedFilters.search) params.append("search", debouncedFilters.search);
        if (debouncedFilters.category) params.append("category", debouncedFilters.category);

        const response = await fetch(`http://localhost:3001/api/pantry/search?${params.toString()}`);
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
  }, [debouncedFilters]);

  const clearFilters = useCallback(() => setFilters({ search: "", category: "" }), []);

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
