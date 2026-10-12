# System Architecture: Pantry Tracker PWA

> **Demo output** — produced by running the `create-architecture` skill (RT-only stub, no Context or Constraints). This is intentionally generic. The architecture lacks platform-specific constraints, non-functional requirements, and technology decisions that Context and Constraints would provide.

---

## Major Components

### 1. Pantry Service
A dedicated backend service responsible for storing, retrieving, and managing pantry items. Exposes a REST API for adding, editing, removing, and listing pantry items per user.

**Responsibilities:**
- Store per-user pantry items (name, quantity, category, expiration date, barcode)
- Validate item data against allowed types and ranges
- Serve pantry list queries sorted by expiration date
- Handle item-level CRUD operations with optimistic concurrency

### 2. Shopping List Service
A backend service that generates and manages shopping lists derived from pantry state and user input.

**Responsibilities:**
- Auto-generate shopping list entries from depleted or low-stock pantry items
- Allow manual additions and removals by the user
- Track check-off state for items during shopping trips
- Provide a "post-shopping" flow to convert checked-off items back into pantry entries

### 3. Barcode Lookup Service
A service that resolves product barcodes to item metadata (name, category, default image).

**Responsibilities:**
- Accept a barcode string and return product information
- Cache lookup results to reduce external API calls
- Fall back gracefully when a barcode is not found
- Support adding new barcode-to-product mappings when users manually correct a lookup result

### 4. Client UI (React + shadcn/Tailwind)
The user-facing PWA built with React and styled using shadcn/ui components and Tailwind CSS.

**Responsibilities:**
- Render the pantry list, shopping list, and add/edit interfaces
- Manage offline-first state using IndexedDB for local persistence
- Register and communicate with a service worker for caching and background sync
- Handle optimistic UI updates and reconciliation when sync completes or fails
- Provide installable PWA behavior (web app manifest, add-to-home-screen)

## Component Interactions

```
[Client UI (React/shadcn)] ←→ [Service Worker] ←→ [IndexedDB]
         │
         ↓ (REST API, background sync)
[Express API Gateway]
         │
    ┌────┼────┐
    ↓    ↓    ↓
[Pantry] [Shopping] [Barcode Lookup]
[Service] [List Svc]    [Service]
```

1. The Client UI reads from and writes to IndexedDB locally, providing full offline functionality. The service worker intercepts fetch requests and serves cached data when the network is unavailable.
2. When connectivity returns, the service worker flushes the sync queue to the Express API gateway, which routes requests to the Pantry Service or Shopping List Service.
3. The Barcode Lookup Service is called directly from the Client UI for real-time scan lookups, with results cached locally in IndexedDB for offline reuse.
4. The Shopping List Service queries the Pantry Service to generate auto-suggested shopping items based on current pantry state.

## Key Technical Decisions

- **Offline-first with IndexedDB:** All pantry data is stored locally in IndexedDB, enabling full app functionality without a network connection. The server is the source of truth, but the client operates independently and syncs when possible.
- **Service worker for caching and background sync:** A service worker caches the app shell (HTML, JS, CSS, assets) and implements a background sync queue for deferred API calls. This ensures the PWA is installable and resilient to connectivity loss.
- **Express/TypeScript backend:** The API gateway and all services are implemented in TypeScript with Express. This provides type safety across the stack and aligns with the React/TypeScript frontend.
- **React with shadcn/ui and Tailwind:** The frontend uses React with shadcn/ui components (Card, Badge, Sheet, Dialog) for consistent, accessible UI. Tailwind CSS handles responsive, mobile-first styling.
- **Last-write-wins sync:** For the initial version, sync conflicts are resolved with a last-write-wins policy. This is simple to implement but may result in data loss when two offline devices edit the same item. A more sophisticated conflict resolution strategy is deferred to a future version.
- **No authentication in initial scope:** The initial architecture assumes a single-user household without authentication. Multi-user and shared-pantry features are out of scope for v1 and would require adding identity management.
- **External barcode API:** Barcode lookups are delegated to an external product database API. No custom product database is built for the initial version; user-corrected lookups are cached but not contributed back to the external source.