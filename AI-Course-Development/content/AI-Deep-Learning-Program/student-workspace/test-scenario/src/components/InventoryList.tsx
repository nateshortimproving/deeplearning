import React, { useEffect, useState } from 'react';

interface Item {
  id: string;
  name: string;
  category: string;
  quantity: number;
}

export const InventoryList: React.FC = () => {
  const [items, setItems] = useState<Item[]>([]);

  useEffect(() => {
    fetch('/api/pantry/items')
      .then((res) => res.json())
      .then((data) => setItems(data));
  }, []);

  // FAILURE: Items are not grouped by category
  // AC2 requires "item is grouped by category"
  
  return (
    <div>
      <h2>Inventory ({items.length} items)</h2>
      <ul>
        {items.map((item) => (
          <li key={item.id}>
            {item.name} - {item.quantity}
          </li>
        ))}
      </ul>
    </div>
  );
};
