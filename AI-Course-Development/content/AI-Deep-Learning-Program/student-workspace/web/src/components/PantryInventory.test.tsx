import { describe, expect, it, beforeEach, vi } from "vitest";
import { render, screen, fireEvent, waitFor } from "@testing-library/react";
import { PantryInventory } from "./PantryInventory";

global.fetch = vi.fn();

const milk = { id: "1", name: "Milk", quantity: 1, unit: "gallon", category: "Dairy", expirationDate: "2026-10-20" };
const apples = { id: "2", name: "Apples", quantity: 4, unit: "count", category: "Produce", expirationDate: "2026-10-18" };

const mockApi = (search: (url: string) => unknown[], categories: string[] = []) => {
  vi.mocked(global.fetch).mockImplementation((async (url: string) => ({
    ok: true,
    json: async () =>
      url.includes("/categories") ? { categories } : { items: search(url), count: search(url).length },
  })) as unknown as typeof fetch);
};

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
    mockApi((url) => (url.includes("search=Milk") ? [milk] : [milk, apples]));

    render(<PantryInventory />);
    fireEvent.change(screen.getByLabelText("Search"), { target: { value: "Milk" } });

    await waitFor(() => {
      expect(global.fetch).toHaveBeenCalledWith(expect.stringContaining("search=Milk"));
      expect(screen.queryByText(/Apples/)).not.toBeInTheDocument();
      expect(screen.getByText(/Milk/)).toBeInTheDocument();
    });
  });

  it("calls /api/pantry/search when category filter changes", async () => {
    mockApi((url) => (url.includes("category=Produce") ? [apples] : [milk, apples]), ["Dairy", "Produce"]);

    render(<PantryInventory />);
    await waitFor(() => expect(screen.getByRole("option", { name: "Produce" })).toBeInTheDocument());
    fireEvent.change(screen.getByLabelText("Category"), { target: { value: "Produce" } });

    await waitFor(() => {
      expect(global.fetch).toHaveBeenCalledWith(expect.stringContaining("category=Produce"));
      expect(screen.queryByText(/Milk/)).not.toBeInTheDocument();
      expect(screen.getByText(/Apples/)).toBeInTheDocument();
    });
  });

  it("renders empty state when filters match no items", async () => {
    mockApi((url) => (url.includes("search=NonExistent") ? [] : [milk]));

    render(<PantryInventory />);
    fireEvent.change(screen.getByLabelText("Search"), { target: { value: "NonExistent" } });

    await waitFor(() => {
      expect(screen.getByTestId("empty-state")).toBeInTheDocument();
      expect(screen.getByText("No items match your filters.")).toBeInTheDocument();
    });
  });

  it("clears filters when clear button is clicked", async () => {
    mockApi((url) => (url.includes("search=NonExistent") ? [] : [milk]));

    render(<PantryInventory />);
    fireEvent.change(screen.getByLabelText("Search"), { target: { value: "NonExistent" } });
    await waitFor(() => expect(screen.getByTestId("empty-state")).toBeInTheDocument());

    fireEvent.click(screen.getByText("Clear filters"));

    await waitFor(() => {
      expect(screen.queryByTestId("empty-state")).not.toBeInTheDocument();
      expect(screen.getByText(/Milk/)).toBeInTheDocument();
    });
  });
});
