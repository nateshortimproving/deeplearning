import React from "react";
import type { PantryItem } from "../types/pantry";
import { usePantryFilter } from "../hooks/usePantryFilter";
import { EmptyState } from "./EmptyState";

interface PantryInventoryProps {
  items: PantryItem[];
}

export function PantryInventory({ items }: PantryInventoryProps) {
  const categories = Array.from(new Set(items.map((item) => item.category))).sort();
  const { filters, setFilters, clearFilters, filteredItems, hasActiveFilters } = usePantryFilter(
    items,
    categories
  );

  return (
    <div>
      <h1>Pantry Inventory</h1>

      <label htmlFor="pantry-search">Search</label>
      <input
        id="pantry-search"
        type="text"
        value={filters.search}
        onChange={(e) => setFilters({ ...filters, search: e.target.value })}
        placeholder="Search items..."
      />

      <label htmlFor="pantry-category">Category</label>
      <select
        id="pantry-category"
        value={filters.category}
        onChange={(e) => setFilters({ ...filters, category: e.target.value })}
      >
        <option value="">All categories</option>
        {categories.map((category) => (
          <option key={category} value={category}>
            {category}
          </option>
        ))}
      </select>

      {filteredItems.length === 0 && hasActiveFilters ? (
        <EmptyState onClearFilters={clearFilters} />
      ) : (
        <ul aria-label="Pantry items">
          {filteredItems.map((item) => (
            <li key={item.id}>
              {item.name} — {item.quantity} {item.unit} ({item.category})
            </li>
          ))}
        </ul>
      )}
    </div>
  );
}
