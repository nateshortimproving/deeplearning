import React from "react";
import { usePantryFilter } from "../hooks/usePantryFilter";
import { EmptyState } from "./EmptyState";

/**
 * Pantry Inventory component with search and category filter.
 * PANTRY-005-AC1, AC2, AC3: Calls /api/pantry/search API endpoint.
 */
export function PantryInventory() {
  const { filters, setFilters, clearFilters, items, categories, loading, error, hasActiveFilters } =
    usePantryFilter();

  return (
    <div>
      <h1>Pantry Inventory</h1>

      {error && <div role="alert">{error}</div>}

      <label htmlFor="pantry-search">Search</label>
      <input
        id="pantry-search"
        type="text"
        value={filters.search}
        onChange={(e) => setFilters({ ...filters, search: e.target.value })}
        placeholder="Search items..."
        disabled={loading}
      />

      <label htmlFor="pantry-category">Category</label>
      <select
        id="pantry-category"
        value={filters.category}
        onChange={(e) => setFilters({ ...filters, category: e.target.value })}
        disabled={loading}
      >
        <option value="">All categories</option>
        {categories.map((category) => (
          <option key={category} value={category}>
            {category}
          </option>
        ))}
      </select>

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
