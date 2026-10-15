# PANTRY-005 Implementation: Filter and Search Inventory

This workspace contains a full-stack implementation of the PANTRY-005 story (Filter and Search Inventory) using:
- **Backend:** Fastify + Prisma + PostgreSQL
- **Frontend:** React + TypeScript

## Quick Start

### Prerequisites
- Node.js 18+
- PostgreSQL 12+
- npm or yarn

### Setup

1. **Create the database:**
   ```bash
   createdb pantrypal
   ```

2. **Set up environment variables:**
   ```bash
   cd api
   cp .env.example .env
   # Edit .env and set DATABASE_URL to your PostgreSQL connection string
   ```

3. **Install dependencies and run migrations:**
   ```bash
   cd api
   npm install
   npm run db:migrate
   npm run db:seed
   ```

4. **Install frontend dependencies:**
   ```bash
   cd ../web
   npm install
   ```

### Running Tests

**Backend tests:**
```bash
cd api
npm test
```

**Frontend tests:**
```bash
cd web
npm test
```

### Running the App

**Start the API server:**
```bash
cd api
npm run dev
# Server runs on http://localhost:3000
```

**In another terminal, start the web client:**
```bash
cd web
npm run dev
# Client runs on http://localhost:5173
```

Then open `http://localhost:5173` in your browser.

## Project Structure

```
.
├── api/
│   ├── src/
│   │   ├── services/
│   │   │   └── PantryService.ts       # Search/filter logic
│   │   ├── routes/
│   │   │   └── pantry.ts              # API endpoints
│   │   ├── types/
│   │   │   └── pantry.ts              # TypeScript types
│   │   └── seed.ts                    # Database seeding
│   ├── prisma/
│   │   ├── schema.prisma              # Database schema
│   │   └── migrations/                # Database migrations
│   ├── package.json
│   └── .env.example
├── web/
│   ├── src/
│   │   ├── components/
│   │   │   ├── PantryInventory.tsx    # Main UI component
│   │   │   └── EmptyState.tsx         # Empty state UI
│   │   ├── hooks/
│   │   │   └── usePantryFilter.ts     # API integration hook
│   │   └── types/
│   │       └── pantry.ts              # TypeScript types
│   └── package.json
├── plan.yaml                          # Implementation plan
├── stories.yaml                       # User stories
└── evaluation-criteria.md             # Quality criteria
```

## Implementation Details

### Backend (API)

**PantryService** provides three methods:
- `searchByName(searchText)` — Search items by name (case-insensitive, partial match)
- `filterByCategory(category)` — Filter items by category
- `searchAndFilter(searchText, category)` — Combined search and filter

**API Endpoints:**
- `GET /api/pantry/search?search=...&category=...` — Search and filter items
- `GET /api/pantry/categories` — Get all unique categories

### Frontend (Web)

**usePantryFilter hook:**
- Manages filter state (search text, category)
- Calls `/api/pantry/search` when filters change
- Handles loading and error states

**PantryInventory component:**
- Renders search input and category dropdown
- Displays filtered items or empty state
- Calls the hook to manage state and API calls

## Acceptance Criteria

- **AC1:** When user types in search field, only items matching the search text are shown
- **AC2:** When user selects a category, only items in that category are shown
- **AC3:** When filters match no items, empty state is shown with a "Clear filters" button

## Testing

All code is tested with:
- **Backend:** Vitest + mocked Prisma
- **Frontend:** Vitest + React Testing Library + mocked fetch

Run tests with `npm test` in either directory.

## Notes

- Search is case-insensitive and supports partial matches
- Filters use AND logic (both must match)
- Empty filters return no results (not all items)
- Database uses indexes on `name` and `category` for performance
