export interface PantryItem {
  id: string;
  name: string;
  quantity: number;
  unit: string;
  category: string;
  expirationDate: string;
}

export interface SearchAndFilterResponse {
  items: PantryItem[];
  count: number;
}
