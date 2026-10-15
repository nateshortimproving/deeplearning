import React, { useCallback } from "react";
import { usePantryFilter } from "../hooks/usePantryFilter";
import SearchInput from "./SearchInput";
import CategorySelect from "./CategorySelect";
import EmptyState from "./EmptyState";

/**
 * Pantry Inventory component with search and category filter.
 * PANTRY-005-AC1, AC2, AC3: Calls /api/pantry/search API endpoint.
 */
export function PantryInventory() {
  const { filters, setFilters, clearFilters, items, categories, loading, error, hasActiveFilters } =
    usePantryFilter();

  const handleSearchChange = useCallback((e: React.ChangeEvent<HTMLInputElement>) => {
    setFilters((prev) => ({ ...prev, search: e.target.value }));
  }, [setFilters]);

  const handleCategoryChange = useCallback((e: React.ChangeEvent<HTMLSelectElement>) => {
    setFilters((prev) => ({ ...prev, category: e.target.value }));
  }, [setFilters]);

  return (
    <div>
      <h1>Pantry Inventory</h1>

      {error && <div role="alert">{error}</div>}

      <SearchInput value={filters.search} onChange={handleSearchChange} />

      <CategorySelect
        value={filters.category}
        onChange={handleCategoryChange}
        categories={categories}
      />

      {loading && <p>Loading...</p>}

      {items.length === 0 && hasActiveFilters && !loading ? (
        <EmptyState onClearFilters={clearFilters} />
      ) : (
        <ul aria-label="Pantry items">
          {items.map((item) => (
            <li key={item.id}>
              {item.name} — {item.quantity} {item.unit} ({item.category})
            </li>
          ))}
        </ul>
      )}
    </div>
  );
}

export default PantryInventory;
