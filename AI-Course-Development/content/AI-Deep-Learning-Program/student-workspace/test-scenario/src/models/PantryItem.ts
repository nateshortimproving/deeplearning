// PantryItem model - INTENTIONAL GAP: Missing validation
export interface PantryItem {
  id: string;
  name: string;
  category: string;
  quantity: number;
  expirationDate?: Date;
  createdAt: Date;
  updatedAt: Date;
}

export class PantryItemModel {
  static create(data: Partial<PantryItem>): PantryItem {
    // FAILURE: No validation of required fields
    // AC1 requires "required information" but this accepts anything
    return {
      id: Math.random().toString(),
      name: data.name || '',
      category: data.category || '',
      quantity: data.quantity || 0,
      expirationDate: data.expirationDate,
      createdAt: new Date(),
      updatedAt: new Date(),
    };
  }
}
