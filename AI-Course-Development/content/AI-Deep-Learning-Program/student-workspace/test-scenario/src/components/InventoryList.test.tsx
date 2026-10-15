import { render, screen } from '@testing-library/react';
import { InventoryList } from './InventoryList';

describe('InventoryList', () => {
  // FAILURE: No test for AC2 (items grouped by category)
  
  it('should render inventory list', () => {
    render(<InventoryList />);
    expect(screen.getByText(/Inventory/)).toBeInTheDocument();
  });
});
