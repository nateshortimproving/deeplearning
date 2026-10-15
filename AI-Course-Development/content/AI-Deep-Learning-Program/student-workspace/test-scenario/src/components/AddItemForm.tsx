import React, { useState } from 'react';

export const AddItemForm: React.FC = () => {
  const [formData, setFormData] = useState({
    name: '',
    category: '',
    quantity: 0,
  });

  const handleSubmit = async (e: React.FormEvent) => {
    e.preventDefault();
    
    // FAILURE: No validation before submit
    // AC3 requires validation message when required field is empty
    // This code will submit even with empty name/category
    
    const response = await fetch('/api/pantry/items', {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify(formData),
    });

    if (response.ok) {
      setFormData({ name: '', category: '', quantity: 0 });
      // FAILURE: No success confirmation shown to user
      // AC1 requires "success confirmation"
    }
  };

  return (
    <form onSubmit={handleSubmit}>
      <input
        type="text"
        placeholder="Item name"
        value={formData.name}
        onChange={(e) => setFormData({ ...formData, name: e.target.value })}
      />
      <select
        value={formData.category}
        onChange={(e) => setFormData({ ...formData, category: e.target.value })}
      >
        <option value="">Select category</option>
        <option value="produce">Produce</option>
        <option value="dairy">Dairy</option>
      </select>
      <input
        type="number"
        placeholder="Quantity"
        value={formData.quantity}
        onChange={(e) => setFormData({ ...formData, quantity: parseInt(e.target.value) })}
      />
      <button type="submit">Add Item</button>
    </form>
  );
};
