import React, { memo } from "react";

interface SearchInputProps {
  value: string;
  onChange: (e: React.ChangeEvent<HTMLInputElement>) => void;
}

const SearchInput = memo(function SearchInput({ value, onChange }: SearchInputProps) {
  return (
    <>
      <label htmlFor="pantry-search">Search</label>
      <input
        id="pantry-search"
        type="text"
        value={value}
        onChange={onChange}
        placeholder="Search items..."
      />
    </>
  );
});

export default SearchInput;
