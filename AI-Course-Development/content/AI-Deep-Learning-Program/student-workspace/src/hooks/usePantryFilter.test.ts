import { describe, expect, it } from "vitest";
import { renderHook, act } from "@testing-library/react";
import { usePantryFilter } from "./usePantryFilter";
import type { PantryItem } from "../types/pantry";

const sampleItems: PantryItem[] = [
  { id: "1", name: "Milk", quantity: 1, unit: "gallon", category: "Dairy", expirationDate: "2026-10-20" },
  { id: "2", name: "Eggs", quantity: 12, unit: "count", category: "Dairy", expirationDate: "2026-10-25" },
  { id: "3", name: "Apples", quantity: 4, unit: "count", category: "Produce", expirationDate: "2026-10-18" },
];

const categories = ["Dairy", "Produce"];

describe("usePantryFilter", () => {
  it("returns only items matching the search text (case-insensitive, partial)", () => {
    const { result } = renderHook(() => usePantryFilter(sampleItems, categories));

    act(() => {
      result.current.setFilters({ ...result.current.filters, search: "ilk" });
    });

    expect(result.current.filteredItems).toHaveLength(1);
    expect(result.current.filteredItems[0].name).toBe("Milk");
  });

  it("returns only items matching the selected category", () => {
    const { result } = renderHook(() => usePantryFilter(sampleItems, categories));

    act(() => {
      result.current.setFilters({ ...result.current.filters, category: "Produce" });
    });

    expect(result.current.filteredItems).toHaveLength(1);
    expect(result.current.filteredItems[0].name).toBe("Apples");
  });

  it("returns no items and reports active filters when search and category together match nothing", () => {
    const { result } = renderHook(() => usePantryFilter(sampleItems, categories));

    act(() => {
      result.current.setFilters({ search: "Milk", category: "Produce" });
    });

    expect(result.current.filteredItems).toHaveLength(0);
    expect(result.current.hasActiveFilters).toBe(true);
  });

  it("clears all filters when clearFilters is called", () => {
    const { result } = renderHook(() => usePantryFilter(sampleItems, categories));

    act(() => {
      result.current.setFilters({ search: "Milk", category: "Dairy" });
    });

    act(() => {
      result.current.clearFilters();
    });

    expect(result.current.filters).toEqual({ search: "", category: "" });
    expect(result.current.filteredItems).toHaveLength(sampleItems.length);
  });
});
