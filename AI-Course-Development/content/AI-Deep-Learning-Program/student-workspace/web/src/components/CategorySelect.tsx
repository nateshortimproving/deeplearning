import React, { memo, useMemo } from "react";

interface CategorySelectProps {
  value: string;
  onChange: (e: React.ChangeEvent<HTMLSelectElement>) => void;
  categories: string[];
}

const CategorySelect = memo(function CategorySelect({ value, onChange, categories }: CategorySelectProps) {
  const categoryOptions = useMemo(() => {
    return categories.map((category) => (
      <option key={category} value={category}>
        {category}
      </option>
    ));
  }, [categories]);

  return (
    <>
      <label htmlFor="pantry-category">Category</label>
      <select
        id="pantry-category"
        value={value}
        onChange={onChange}
      >
        <option value="">All categories</option>
        {categoryOptions}
      </select>
    </>
  );
});

export default CategorySelect;
