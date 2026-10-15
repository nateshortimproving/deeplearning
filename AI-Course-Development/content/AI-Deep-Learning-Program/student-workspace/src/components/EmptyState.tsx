import React from "react";

interface EmptyStateProps {
  onClearFilters: () => void;
}

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
