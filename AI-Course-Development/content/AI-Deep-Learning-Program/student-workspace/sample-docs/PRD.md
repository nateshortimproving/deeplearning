# PRD: PantryPal — Pantry Inventory & Shopping List

## Problem Statement
Home cooks lose money and time in two connected ways: food spoils unnoticed in the back of the pantry because there is no lightweight way to track what's on hand and when it expires, and grocery trips are inefficient because shopping lists are built from memory rather than from actual inventory levels. Existing grocery list apps are disconnected from what's actually in the pantry, so lists are incomplete, duplicate items get bought, and low-stock essentials get missed. Households that shop together also lack a shared, real-time view of the list, leading to duplicate purchases or missed items when more than one person shops.

## Proposed Solution
PantryPal is a connected pantry inventory and shopping list application. Users maintain a digital pantry with quantities, categories, and expiration dates. The app surfaces expiration risk with visual urgency indicators and automatically suggests shopping list items when pantry stock falls below a defined threshold. Users can also add ad-hoc items to the list, check items off during a shopping trip, and sync purchases back into pantry inventory in one action — closing the loop between "what I bought" and "what I have." Lists can be shared with a household member so both parties see live updates while shopping.

## Success Metrics
- 70%+ of pantry items added have an expiration date populated within 30 days of launch (indicates the expiration feature is trusted enough to use)
- 50% reduction in items marked "Empty"/zero-quantity that were also flagged expired in the same edit (proxy for reduced food waste)
- 60%+ of shopping list items originate from auto-suggestion (vs. 100% manual entry), indicating the suggestion engine is providing real value
- 80%+ of completed shopping trips use "Add All to Pantry" sync rather than manual re-entry
- Shared lists show a second participant within 7 days of first share for 30%+ of households that use sharing
- Real-time checkbox updates propagate to a second viewer in under 3 seconds for 95% of sessions

## Scope

### In Scope
- Manual add / edit / delete (with confirmation) of pantry items: name, quantity, unit, category, purchase date, expiration date, low-stock threshold, target stock level
- Color-coded expiration urgency badges and an app-level "expiring soon" banner with filtered view
- Search and category filtering of pantry inventory
- Auto-suggested shopping list items derived from low-stock/out-of-stock pantry items, with suggested buy quantity
- Manual addition of ad-hoc items to the shopping list, with a duplicate-name hint against existing pantry items
- Checking off purchased items during a shopping trip, with a "Shopping Complete" completion state
- One-action sync of purchased items back into pantry inventory (match by name, update quantity; create new item if unmatched), with duplicate-sync confirmation
- Shareable shopping list links with real-time (near real-time, ≤3s) synchronized purchased/unpurchased state across viewers
- Toast/summary feedback for sync, save, and error actions

### Out of Scope
- Barcode/receipt scanning for pantry entry
- Recipe suggestions or meal planning based on pantry contents
- Multi-household or multi-pantry management per user
- Push notifications (expiration and completion states are in-app only in v1)
- Payment, price tracking, or store integration
- Native mobile apps (web/PWA only)
- User roles/permissions beyond "anyone with the share link can edit"

## Assumptions
- A single pantry belongs to one household; "sharing" applies to the shopping list, not separate pantry access control, in v1
- Users are trusted collaborators once they have a share link — no per-user granular permissions are needed for v1
- Item name matching for shopping-to-pantry sync uses simple case-insensitive exact match; fuzzy matching is not required for v1
- Users are willing to manually enter expiration dates; automatic expiration lookup (e.g., by barcode) is not required for v1
- "Today" for purchase-date stamping is the device's local date at the time of sync

## Open Questions
- Should low-stock thresholds and target stock levels have sensible category-based defaults, or must every item be configured manually?
- How long should a share link remain valid, and can it be revoked/regenerated?
- What happens to a shared list's real-time session if a participant is offline when changes occur — do they see a diff or just the latest state on reconnect?
- Is there a limit to how many pantry items or shopping list items a household can maintain before pagination/virtualization is required?
- Should "Uncategorized" items created via sync be flagged for the user to later categorize, and if so, where?
