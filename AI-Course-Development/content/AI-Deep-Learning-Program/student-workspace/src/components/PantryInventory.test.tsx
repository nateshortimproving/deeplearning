import { describe, expect, it } from "vitest";
import { render, screen, fireEvent } from "@testing-library/react";
import { PantryInventory } from "./PantryInventory";
import type { PantryItem } from "../types/pantry";

const sampleItems: PantryItem[] = [
  { id: "1", name: "Milk", quantity: 1, unit: "gallon", category: "Dairy", expirationDate: "2026-10-20" },
  { id: "2", name: "Eggs", quantity: 12, unit: "count", category: "Dairy", expirationDate: "2026-10-25" },
  { id: "3", name: "Apples", quantity: 4, unit: "count", category: "Produce", expirationDate: "2026-10-18" },
];

describe("PantryInventory", () => {
  it("renders a search field and a category filter", () => {
    render(<PantryInventory items={sampleItems} />);

    expect(screen.getByLabelText("Search")).toBeInTheDocument();
    expect(screen.getByLabelText("Category")).toBeInTheDocument();
  });

  it("shows only items matching the search text", () => {
    render(<PantryInventory items={sampleItems} />);

    fireEvent.change(screen.getByLabelText("Search"), { target: { value: "Milk" } });

    expect(screen.getByText("Milk")).toBeInTheDocument();
    expect(screen.queryByText("Eggs")).not.toBeInTheDocument();
    expect(screen.queryByText("Apples")).not.toBeInTheDocument();
  });

  it("shows only items in the selected category", () => {
    render(<PantryInventory items={sampleItems} />);

    fireEvent.change(screen.getByLabelText("Category"), { target: { value: "Produce" } });

    expect(screen.getByText("Apples")).toBeInTheDocument();
    expect(screen.queryByText("Milk")).not.toBeInTheDocument();
    expect(screen.queryByText("Eggs")).not.toBeInTheDocument();
  });

  it("renders the empty state when filters match no items and clears filters on button click", () => {
    render(<PantryInventory items={sampleItems} />);

    fireEvent.change(screen.getByLabelText("Search"), { target: { value: "Milk" } });
    fireEvent.change(screen.getByLabelText("Category"), { target: { value: "Produce" } });

    expect(screen.getByTestId("empty-state")).toBeInTheDocument();
    expect(screen.getByText("No items match your filters.")).toBeInTheDocument();

    fireEvent.click(screen.getByText("Clear filters"));

    expect(screen.queryByTestId("empty-state")).not.toBeInTheDocument();
    expect(screen.getByText("Milk")).toBeInTheDocument();
    expect(screen.getByText("Apples")).toBeInTheDocument();
  });
});
