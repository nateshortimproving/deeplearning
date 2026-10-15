import React from "react";

interface EmptyStateProps {
  onClearFilters: () => void;
}

/**
 * Empty state component shown when filters match no items.
 * PANTRY-005-AC3: Renders when the API returns no results.
 */
export function EmptyState({ onClearFilters }: EmptyStateProps) {
  return (
    <div data-testid="empty-state">
      <p>No items match your filters.</p>
      <button type="button" onClick={onClearFilters}>
        Clear filters
      </button>
    </div>
  );
}
