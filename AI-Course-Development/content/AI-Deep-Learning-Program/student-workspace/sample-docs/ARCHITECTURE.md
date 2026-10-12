# Architecture: PantryPal — Pantry Inventory & Shopping List

## Overview
PantryPal is built as a Node.js/TypeScript full-stack application: a single Fastify-based API service backed by PostgreSQL (via Prisma ORM), with a Socket.IO layer for real-time shopping list collaboration. The system is organized around two core domains — Pantry and Shopping List — plus a Sync component that bridges them, and a lightweight Sharing component that issues tokenized links for collaborative lists. Business logic (threshold-based suggestion, expiration-urgency calculation, sync matching) lives in the API layer as plain TypeScript services, kept independent of HTTP/WebSocket transport so they're unit-testable and reusable between the REST and real-time paths.

The real-time requirement (shared list updates visible within 3 seconds) is met by having the checkbox-toggle and list-mutation endpoints both persist to Postgres and emit a Socket.IO event to a room keyed by `shareToken`; connected clients apply the event optimistically without a full refetch. All other interactions are standard request/response over REST, keeping the system easy to reason about and to extend with a mobile client later without depending on WebSocket state.

## Components

### API Server (Fastify + TypeScript)
- **Responsibility:** Hosts REST endpoints for pantry CRUD, shopping list CRUD, sync, and share-link issuance; validates input; orchestrates domain services; emits real-time events.
- **Interfaces:** `/api/pantry/*`, `/api/shopping-list/*`, `/api/sync`, `/api/share/*` (JSON over HTTPS); a Socket.IO namespace `/shopping-list` for real-time events (`item:updated`, `list:completed`)
- **Dependencies:** Prisma Client, Pantry Service, Shopping List Service, Sync Service, Sharing Service

### Pantry Service
- **Responsibility:** Owns pantry item lifecycle (create/edit/delete), category grouping, search/filter query logic, and expiration-urgency classification (green/yellow/red/grey/expired banding based on days-to-expiration)
- **Interfaces:** `PantryService.create()`, `.update()`, `.delete()`, `.list(filters)`, `.getExpiringSoon(days)` — called by API route handlers
- **Dependencies:** Prisma Client (PostgreSQL), a pure `expirationBanding()` utility (no external deps, unit-testable)

### Shopping List Service
- **Responsibility:** Owns shopping list item lifecycle (auto-suggested + manual), the low-stock suggestion algorithm (target level − current quantity, out-of-stock badge), purchased/unpurchased state, and "Shopping Complete" detection
- **Interfaces:** `ShoppingListService.getSuggestions()`, `.addManualItem()`, `.togglePurchased()`, `.isComplete()` — called by API route handlers and the Socket.IO event emitter
- **Dependencies:** Prisma Client, Pantry Service (reads thresholds/quantities to compute suggestions)

### Sync Service
- **Responsibility:** Moves purchased shopping list items back into pantry inventory — matches by case-insensitive name, increments existing pantry quantity or creates a new "Uncategorized" pantry item, stamps purchase date, clears the shopping list, and guards against duplicate syncs per shopping trip
- **Interfaces:** `SyncService.syncPurchasesToPantry(shoppingListId)` returning a summary (`itemsAdded`, `itemsUpdated`) for the toast message
- **Dependencies:** Pantry Service, Shopping List Service, Prisma Client (transactional write across both tables)

### Sharing Service
- **Responsibility:** Issues and validates opaque, unguessable share tokens for a shopping list; resolves a token to a list ID for both REST reads and Socket.IO room joins
- **Interfaces:** `SharingService.createShareLink(listId)`, `.resolveToken(token)`
- **Dependencies:** Prisma Client (share token table with expiry column reserved for future use)

### Real-Time Gateway (Socket.IO)
- **Responsibility:** Maintains a room per `shareToken`; on any shopping list mutation, the API broadcasts the updated item/list state to that room so all connected viewers converge within the 3-second target
- **Interfaces:** Socket.IO events `join:list`, `item:updated`, `list:completed`
- **Dependencies:** Shopping List Service (as the source of truth for broadcast payloads)

### Web Client (React + TypeScript PWA)
- **Responsibility:** Renders pantry and shopping list UI, manages optimistic UI updates for checkbox toggles, subscribes to Socket.IO for shared-list updates, and works offline-tolerant for read views via a service worker cache
- **Interfaces:** Consumes the REST API and Socket.IO namespace described above
- **Dependencies:** API Server (documented in the UX/architecture-facing OpenAPI contract)

### Database (PostgreSQL)
- **Responsibility:** Durable storage for `PantryItem`, `ShoppingListItem`, `ShareLink`, and `SyncLog` (used to guard against duplicate syncs) tables
- **Interfaces:** Accessed exclusively through Prisma Client from the API Server — no other component talks to Postgres directly
- **Dependencies:** None (leaf component)

## Data Flow
1. **Pantry maintenance:** Client → REST `/api/pantry` → Pantry Service → Prisma → Postgres; response re-renders the categorized inventory list.
2. **Suggestion generation:** Client loads shopping list page → REST `/api/shopping-list/suggestions` → Shopping List Service reads pantry quantities/thresholds via Pantry Service → returns suggested items with computed buy quantity.
3. **Shopping trip:** Client toggles a checkbox → REST `/api/shopping-list/:id/toggle` → Shopping List Service updates Postgres → API emits `item:updated` over Socket.IO to the list's room → all connected clients (including the toggling client, for consistency) update from the broadcast rather than the HTTP response alone.
4. **Sync to pantry:** Client clicks "Add All to Pantry" → REST `/api/sync` → Sync Service checks `SyncLog` for an existing sync on this trip (prompts confirmation if found) → within a DB transaction, updates/creates Pantry items and clears the Shopping List → returns a summary → client shows toast and clears local list state.
5. **Sharing:** Client clicks "Share" → REST `/api/share` → Sharing Service creates a token, returns a URL → recipient's client opens the URL → REST resolves the token to list data and the client joins the corresponding Socket.IO room for live updates.

## Key Technical Decisions
| Decision | Choice | Rationale |
|----------|--------|-----------|
| Language/runtime | TypeScript on Node.js (LTS) | Type safety shared conceptually across API and client; large ecosystem; team-favored stack |
| API framework | Fastify | Low overhead, first-class TypeScript support, built-in schema validation (JSON Schema/TypeBox) for request/response contracts |
| Database | PostgreSQL | Relational integrity for pantry↔shopping-list matching logic; mature, widely supported |
| ORM | Prisma | Type-safe query client generated from schema; migrations built in; fits TypeScript-first stack |
| Real-time transport | Socket.IO | Simple room-based broadcast model fits the "shared list" use case; automatic fallback/reconnect handling reduces custom code |
| Sync duplicate-guard | Persisted `SyncLog` row per trip, checked before sync | Meets the "warn before duplicate sync" requirement without relying on client-only state that can be lost on refresh |
| Client framework | React (PWA) | Matches team's UX direction (see UX Guidance); component reuse between pantry and shopping list views |
| Monorepo tooling | npm workspaces (`/api`, `/web`, `/shared`) | Shares TypeScript types (e.g., `PantryItem`, `ShoppingListItem`) between client and server without publishing packages |
| Auth for v1 | None (single-household, token-based list sharing only) | Matches PRD scope — no multi-tenant/user-permission requirement in v1; token acts as sole access control for shared lists |

## Constraints
- Real-time shopping list updates must reach a second viewer within 3 seconds (drives the choice of server-push broadcast over polling)
- Sync-to-pantry must be transactional — partial sync (some items added, list not cleared) is not acceptable
- Duplicate sync attempts for the same shopping trip must be detectable and require explicit confirmation
- Share tokens must be unguessable (sufficient entropy) since they are the only access control on a shared list in v1
- The web client must remain usable primarily on mobile viewports during an active shopping trip (network conditions in-store may be poor — optimistic UI updates are required, not just server-confirmed state)
- No native mobile app in v1 — the web/PWA client is the only supported surface
