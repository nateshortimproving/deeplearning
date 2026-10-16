# Architecture: Pantry Tracker PWA

## Overview
An offline-first Progressive Web App backed by a small set of TypeScript
services. The client owns a local copy of pantry state in IndexedDB so every
core flow — checking the pantry, adding items, generating a shopping list —
works in a kitchen with no connectivity; a service worker queues mutations
and syncs when the network returns. Backend services stay thin: they
persist state, resolve barcodes, and reconcile sync batches.

## Components

### Client UI
- **Responsibility:** Renders pantry, alerts, and shopping-list screens; performs barcode scans; maintains offline state and optimistic updates.
- **Interfaces:** PWA shell (React + service worker); REST calls to the Sync Gateway; product lookups on the Barcode Lookup Service.
- **Dependencies:** IndexedDB, service worker, Sync Gateway, Barcode Lookup Service.

### Sync Gateway
- **Responsibility:** Accepts batched mutations and reads from the Client UI, authenticates devices, and routes work to domain services.
- **Interfaces:** REST endpoints `/sync`, `/pantry`, `/shopping-list` consumed by the Client UI.
- **Dependencies:** Pantry Service, Shopping List Service.

### Pantry Service
- **Responsibility:** Owns pantry item state (name, quantity, category, expiration) and computes expiration alerts.
- **Interfaces:** Internal REST API called by the Sync Gateway; item model consumed by the Shopping List Service.
- **Dependencies:** Data Store.

### Shopping List Service
- **Responsibility:** Generates and manages shopping lists from low-stock and expired items, including post-shopping conversion back into pantry entries.
- **Interfaces:** Internal REST API called by the Sync Gateway.
- **Dependencies:** Pantry Service (item state), Data Store.

### Barcode Lookup Service
- **Responsibility:** Resolves scanned barcodes to product metadata with caching and manual-correction support.
- **Interfaces:** REST endpoint called directly by the Client UI.
- **Dependencies:** External product database API, Data Store (cache).

### Data Store
- **Responsibility:** Persists pantry items, shopping lists, and barcode cache entries.
- **Interfaces:** PostgreSQL access via a repository layer used by all backend services.
- **Dependencies:** Managed PostgreSQL.

## Data Flow
The Client UI serves reads from IndexedDB instantly and queues writes via
its service worker. When online, queued mutations flush to the Sync
Gateway, which routes pantry changes to the Pantry Service and list
operations to the Shopping List Service; the Shopping List Service reads
item state from the Pantry Service to build auto-suggestions. Barcode
scans travel directly from the Client UI to the Barcode Lookup Service,
whose results are cached locally. All persistent state lands in the Data
Store.

## Key Technical Decisions
| Decision | Choice | Rationale |
|----------|--------|-----------|
| Offline state model | IndexedDB + service worker background sync | PRD requires full functionality without connectivity in the kitchen |
| Conflict resolution | Last-write-wins | Simplest correct-enough policy for single-user v1; multi-device merge deferred |
| Backend stack | TypeScript/Express services | Shares types and tooling with the React client |
| Identity | None in v1 | PRD scopes out sharing/social features |

## Constraints
- Offline-first is mandatory: pantry read/write and list generation must work with zero connectivity.
- Must be an installable PWA on mobile and desktop (manifest + service worker).
- No authentication or multi-user support in v1 (PRD out-of-scope boundary).
- Recipe suggestions, price tracking, and grocery-store API integrations are excluded.
