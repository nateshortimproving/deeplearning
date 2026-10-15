import { describe, expect, it, beforeEach, vi } from "vitest";
import { renderHook, act, waitFor } from "@testing-library/react";
import { usePantryFilter } from "./usePantryFilter";

global.fetch = vi.fn();

describe("usePantryFilter", () => {
  beforeEach(() => {
    vi.clearAllMocks();
  });

  it("fetches categories on mount", async () => {
    vi.mocked(global.fetch).mockResolvedValueOnce({
      ok: true,
      json: async () => ({ categories: ["Dairy", "Produce"] }),
    } as Response);

    const { result } = renderHook(() => usePantryFilter());

    await waitFor(() => {
      expect(result.current.categories).toEqual(["Dairy", "Produce"]);
    });
  });

  it("fetches items when search filter changes", async () => {
    vi.mocked(global.fetch)
      .mockResolvedValueOnce({
        ok: true,
        json: async () => ({ categories: [] }),
      } as Response)
      .mockResolvedValueOnce({
        ok: true,
        json: async () => ({
          items: [
            { id: "1", name: "Milk", quantity: 1, unit: "gallon", category: "Dairy", expirationDate: "2026-10-20" },
          ],
          count: 1,
        }),
      } as Response);

    const { result } = renderHook(() => usePantryFilter());

    act(() => {
      result.current.setFilters({ search: "Milk", category: "" });
    });

    await waitFor(() => {
      expect(result.current.items).toHaveLength(1);
      expect(result.current.items[0].name).toBe("Milk");
    });
  });

  it("fetches items when category filter changes", async () => {
    vi.mocked(global.fetch)
      .mockResolvedValueOnce({
        ok: true,
        json: async () => ({ categories: ["Dairy", "Produce"] }),
      } as Response)
      .mockResolvedValueOnce({
        ok: true,
        json: async () => ({
          items: [
            { id: "1", name: "Apples", quantity: 4, unit: "count", category: "Produce", expirationDate: "2026-10-18" },
          ],
          count: 1,
        }),
      } as Response);

    const { result } = renderHook(() => usePantryFilter());

    act(() => {
      result.current.setFilters({ search: "", category: "Produce" });
    });

    await waitFor(() => {
      expect(result.current.items).toHaveLength(1);
      expect(result.current.items[0].category).toBe("Produce");
    });
  });

  it("returns empty array when filters match no items", async () => {
    vi.mocked(global.fetch)
      .mockResolvedValueOnce({
        ok: true,
        json: async () => ({ categories: [] }),
      } as Response)
      .mockResolvedValueOnce({
        ok: true,
        json: async () => ({ items: [], count: 0 }),
      } as Response);

    const { result } = renderHook(() => usePantryFilter());

    act(() => {
      result.current.setFilters({ search: "Milk", category: "Produce" });
    });

    await waitFor(() => {
      expect(result.current.items).toHaveLength(0);
      expect(result.current.hasActiveFilters).toBe(true);
    });
  });

  it("clears all filters when clearFilters is called", async () => {
    vi.mocked(global.fetch).mockResolvedValue({
      ok: true,
      json: async () => ({ categories: [], items: [], count: 0 }),
    } as Response);

    const { result } = renderHook(() => usePantryFilter());

    act(() => {
      result.current.setFilters({ search: "Milk", category: "Dairy" });
    });

    act(() => {
      result.current.clearFilters();
    });

    await waitFor(() => {
      expect(result.current.filters).toEqual({ search: "", category: "" });
      expect(result.current.hasActiveFilters).toBe(false);
    });
  });
});
