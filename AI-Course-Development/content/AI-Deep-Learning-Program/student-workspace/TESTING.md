# Testing PANTRY-005

This document walks you through testing the full-stack implementation of PANTRY-005 (Filter and Search Inventory).

## Prerequisites

- **Node.js 18+** — Download from https://nodejs.org/
- **PostgreSQL 12+** — Download from https://www.postgresql.org/download/
- **npm** — Comes with Node.js

## Step 1: Create the Database

```bash
createdb pantrypal
```

If you get an error like "createdb: command not found", you may need to add PostgreSQL to your PATH. On macOS with Homebrew:
```bash
export PATH="/usr/local/opt/postgresql/bin:$PATH"
createdb pantrypal
```

## Step 2: Set Up the API

```bash
cd api
cp .env.example .env
```

Edit `.env` and set `DATABASE_URL` to your PostgreSQL connection string. Example:
```
DATABASE_URL="postgresql://postgres:password@localhost:5432/pantrypal"
```

Then install dependencies and run migrations:
```bash
npm install
npm run db:migrate
npm run db:seed
```

This will:
1. Install all npm packages
2. Run Prisma migrations to create the `pantry_item` table
3. Seed the database with 6 test items (Milk, Eggs, Apples, Carrots, Bread, Rice)

## Step 3: Run Backend Tests

```bash
npm test
```

You should see output like:
```
✓ PantryService (6 tests)
  ✓ searchByName returns items matching the search text
  ✓ searchByName returns empty array for empty search text
  ✓ filterByCategory returns items in the specified category
  ✓ filterByCategory returns empty array for empty category
  ✓ searchAndFilter returns items matching both filters
  ✓ searchAndFilter returns empty array when both filters are empty

✓ Pantry Routes (3 tests)
  ✓ GET /search returns items matching filters
  ✓ GET /search returns empty array when filters match no items
  ✓ GET /search validates query parameters
```

## Step 4: Set Up the Web Client

```bash
cd ../web
npm install
```

## Step 5: Run Frontend Tests

```bash
npm test
```

You should see output like:
```
✓ usePantryFilter (5 tests)
  ✓ fetches categories on mount
  ✓ fetches items when search filter changes
  ✓ fetches items when category filter changes
  ✓ returns empty array when filters match no items
  ✓ clears all filters when clearFilters is called

✓ PantryInventory (5 tests)
  ✓ renders search field and category filter
  ✓ calls /api/pantry/search when search text changes
  ✓ calls /api/pantry/search when category filter changes
  ✓ renders empty state when filters match no items
  ✓ clears filters when clear button is clicked
```

## Step 6: Run the App

Open two terminal windows.

**Terminal 1: Start the API server**
```bash
cd api
npm run dev
```

You should see:
```
Server running at http://localhost:3000
```

**Terminal 2: Start the web client**
```bash
cd web
npm run dev
```

You should see:
```
Local:   http://localhost:5173
```

## Step 7: Test the UI

Open `http://localhost:5173` in your browser.

You should see:
- A "Pantry Inventory" heading
- A search input field
- A category dropdown (with options: All categories, Dairy, Grains, Produce)
- A list of 6 items (Milk, Eggs, Apples, Carrots, Bread, Rice)

### Test Search (AC1)

1. Type "ilk" in the search field
2. Only "Milk" should appear
3. Clear the search field
4. All 6 items should reappear

### Test Category Filter (AC2)

1. Select "Dairy" from the category dropdown
2. Only "Milk" and "Eggs" should appear
3. Select "Produce"
4. Only "Apples" and "Carrots" should appear
5. Select "All categories"
6. All 6 items should reappear

### Test Empty State (AC3)

1. Type "xyz" in the search field
2. Select "Dairy" from the category dropdown
3. The empty state should appear: "No items match your filters."
4. Click "Clear filters"
5. All 6 items should reappear

### Test Combined Filters

1. Type "a" in the search field (matches Apples, Carrots, Bread)
2. Select "Produce" from the category dropdown
3. Only "Apples" and "Carrots" should appear (both start with letters that contain "a" and are in Produce)

## Troubleshooting

### "createdb: command not found"
PostgreSQL is not in your PATH. Install it or add it to your PATH.

### "ECONNREFUSED" when running migrations
PostgreSQL is not running. Start it:
- **macOS (Homebrew):** `brew services start postgresql`
- **macOS (DMG):** Start PostgreSQL.app from Applications
- **Windows:** Start PostgreSQL from Services
- **Linux:** `sudo systemctl start postgresql`

### "database does not exist"
Run `createdb pantrypal` first.

### "npm: command not found"
Node.js is not installed. Download it from https://nodejs.org/

### Tests fail with "Cannot find module"
Run `npm install` in the directory where tests are failing.

## What's Being Tested

### Backend Tests
- **PantryService:** Search by name, filter by category, combined search+filter
- **Routes:** API endpoint validation, query parameter handling

### Frontend Tests
- **usePantryFilter hook:** API calls, state management, filter clearing
- **PantryInventory component:** UI rendering, user interactions, empty state

### Acceptance Criteria
- **AC1:** Search filters items by name (case-insensitive, partial match)
- **AC2:** Category filter shows only items in that category
- **AC3:** Empty state appears when no items match, with "Clear filters" button

## Next Steps

Once tests pass and the UI works as expected:
1. Review the code in `api/src/` and `web/src/`
2. Check the implementation against the plan in `plan.yaml`
3. Read the evaluation criteria in `evaluation-criteria.md`
4. Review the run log in `implement-story-run-log.md`
