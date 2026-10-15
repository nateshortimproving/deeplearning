import { describe, expect, it, beforeEach, vi } from "vitest";
import { render, screen, fireEvent, waitFor } from "@testing-library/react";
import { PantryInventory } from "./PantryInventory";

global.fetch = vi.fn();

describe("PantryInventory", () => {
  beforeEach(() => {
    vi.clearAllMocks();
  });

  it("renders search field and category filter", async () => {
    vi.mocked(global.fetch).mockResolvedValue({
      ok: true,
      json: async () => ({ categories: ["Dairy", "Produce"], items: [], count: 0 }),
    } as Response);

    render(<PantryInventory />);

    expect(screen.getByLabelText("Search")).toBeInTheDocument();
    expect(screen.getByLabelText("Category")).toBeInTheDocument();
  });

  it("calls /api/pantry/search when search text changes", async () => {
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

    render(<PantryInventory />);

    const searchInput = screen.getByLabelText("Search");
    fireEvent.change(searchInput, { target: { value: "Milk" } });

    await waitFor(() => {
      expect(global.fetch).toHaveBeenCalledWith(expect.stringContaining("/api/pantry/search"));
      expect(screen.getByText("Milk")).toBeInTheDocument();
    });
  });

  it("calls /api/pantry/search when category filter changes", async () => {
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

    render(<PantryInventory />);

    const categorySelect = screen.getByLabelText("Category");
    fireEvent.change(categorySelect, { target: { value: "Produce" } });

    await waitFor(() => {
      expect(global.fetch).toHaveBeenCalledWith(expect.stringContaining("category=Produce"));
      expect(screen.getByText("Apples")).toBeInTheDocument();
    });
  });

  it("renders empty state when filters match no items", async () => {
    vi.mocked(global.fetch)
      .mockResolvedValueOnce({
        ok: true,
        json: async () => ({ categories: [] }),
      } as Response)
      .mockResolvedValueOnce({
        ok: true,
        json: async () => ({ items: [], count: 0 }),
      } as Response);

    render(<PantryInventory />);

    const searchInput = screen.getByLabelText("Search");
    fireEvent.change(searchInput, { target: { value: "NonExistent" } });

    await waitFor(() => {
      expect(screen.getByTestId("empty-state")).toBeInTheDocument();
      expect(screen.getByText("No items match your filters.")).toBeInTheDocument();
    });
  });

  it("clears filters when clear button is clicked", async () => {
    vi.mocked(global.fetch)
      .mockResolvedValueOnce({
        ok: true,
        json: async () => ({ categories: [] }),
      } as Response)
      .mockResolvedValueOnce({
        ok: true,
        json: async () => ({ items: [], count: 0 }),
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

    render(<PantryInventory />);

    const searchInput = screen.getByLabelText("Search");
    fireEvent.change(searchInput, { target: { value: "NonExistent" } });

    await waitFor(() => {
      expect(screen.getByTestId("empty-state")).toBeInTheDocument();
    });

    const clearButton = screen.getByText("Clear filters");
    fireEvent.click(clearButton);

    await waitFor(() => {
      expect(screen.queryByTestId("empty-state")).not.toBeInTheDocument();
    });
  });
});
