# UX Guidance: PantryPal — Pantry Inventory & Shopping List

PantryPal is delivered as an installable Progressive Web App (PWA) built with React and shadcn/ui components (Radix primitives + Tailwind CSS), so a single responsive codebase covers the primary in-store mobile experience and the at-home desktop/tablet planning experience. shadcn's Badge, Card, Dialog, Sheet, Checkbox, and Toast (Sonner) components map directly onto this app's core UI needs: expiration urgency badges, item forms, confirmation dialogs, and sync/error feedback.

## User Personas

### The Primary Cook (household pantry owner)
- **Role:** Does most of the cooking and grocery shopping for the household; primary maintainer of pantry data
- **Goals:** Avoid throwing away spoiled food; walk into the store with a complete, trustworthy list; spend minimal time on data entry
- **Pain Points:** Forgets what's already in the pantry and over-buys; discovers expired items only when reaching for them; shopping lists built from memory miss items

### The Co-Shopper (household member)
- **Role:** Occasionally shops for the household, often without having looked at the pantry directly
- **Goals:** Get a reliable list without needing to ask the Primary Cook what's needed; avoid buying duplicates of what's already at home
- **Pain Points:** Receives a verbal or text list that's incomplete; doesn't know if an item on the list was already picked up by someone else while mid-shop

## User Flows

### Flow 1: Add and Track a Pantry Item
1. User taps "Add Item" from the Pantry Inventory page (floating action button on mobile, top-right button on desktop)
2. System opens a shadcn `Sheet` (mobile) or `Dialog` (desktop) with fields: name, quantity, unit, category (`Select`), purchase date, expiration date, low-stock threshold, target stock level
3. User fills the form and taps "Save"
4. System validates required fields (name, quantity, expiration date) inline as the user types/blurs, and again on submit
5. System saves the item, closes the sheet/dialog, and the item appears in its category group in the inventory list with an expiration badge
- **Decision Point:** Whether to set a low-stock threshold/target level now (enables auto-suggestion later) or skip it — the form should make these optional but visually flagged as "recommended for shopping suggestions"
- **Error Risk:** Users skip the expiration date because it feels optional even though it's required; users pick a purchase date after the expiration date without realizing it's inconsistent

### Flow 2: Notice and Act on Expiring Items
1. User opens the app; if any item expires within 7 days, a persistent banner appears at the top of the Pantry Inventory page: "N items expiring soon"
2. User taps the banner
3. System navigates to the same inventory list, pre-filtered to items expiring within 3 days or already expired
4. User reviews the filtered list, each item showing a color-coded badge (green >7 days, yellow 3–7, red <3, grey expired)
5. User either uses the item (edits quantity down/to zero) or deletes it if spoiled
- **Decision Point:** Use it now (edit quantity) vs. discard it (delete) — surface both actions directly from the filtered list, not just the edit form, to avoid an extra navigation step
- **Error Risk:** Color-only badges are inaccessible to colorblind users — badges must always pair color with a text label ("Expires in 2 days", "Expired") per Design Considerations below

### Flow 3: Generate and Complete a Shopping List
1. User navigates to the Shopping List page
2. System shows a "Suggested" section (auto-populated from low-stock/out-of-stock pantry items, each with computed buy quantity) and a "Manual" section (user-added items); if nothing is low, "Suggested" shows "No suggestions — your pantry is well stocked"
3. User optionally taps "Add Item" to add an ad-hoc item via a form (name, quantity, unit, category)
4. If the manual item name matches an existing pantry item, system shows an inline hint: "You may already have this — check your pantry"
5. User goes shopping; for each item, user taps its `Checkbox`, which applies a strikethrough style immediately (optimistic update)
6. Once all items are checked, system shows a "Shopping Complete" banner with an "Add All to Pantry" button
7. User taps "Add All to Pantry"; system syncs purchases into pantry (matching by name, updating quantities, creating new "Uncategorized" items as needed), shows a toast ("N items added to pantry"), and clears the list
- **Decision Point:** Whether to trust an auto-suggested quantity or edit it before shopping — suggested items should remain editable inline, not read-only
- **Error Risk:** Accidental checkbox taps while phone is in a pocket/bag during shopping — the un-check action must be equally obvious and immediate (tap again to restore), and destructive-feeling actions (sync) require the explicit final tap rather than firing automatically on last checkbox

### Flow 4: Share a List with a Co-Shopper
1. Primary Cook taps "Share" on the Shopping List page
2. System generates a link, copies it to the clipboard automatically, and shows a toast: "Link copied"
3. Primary Cook sends the link to the Co-Shopper via their own messaging app (outside PantryPal)
4. Co-Shopper opens the link in a browser (no login required) and sees the live shopping list
5. As either person checks off items, the other's view updates within ~3 seconds, with a brief highlight animation on the changed row so the update is noticeable without a jarring re-render
6. If the list was already fully purchased and synced before the Co-Shopper opens the link, they see a "List Complete" state instead of items
- **Decision Point:** N/A — this flow is intentionally low-friction (no accounts); the only choice is whether to share at all
- **Error Risk:** Co-Shopper thinks the link is a static snapshot and doesn't realize updates are live — a small "Live" indicator with a connection status dot should be persistently visible on shared views

## Key Interactions
- **Expiration badge:** Colored `Badge` + explicit text ("Expires in 2 days" / "Expired") on every pantry item card; never color alone
- **Checkbox toggle (shopping list):** Immediate optimistic strikethrough + muted text color on check; instant reversal on uncheck; underlying sync confirmed via toast only on failure (silent success to avoid noise during rapid checking)
- **"Add All to Pantry":** Primary-emphasis button that appears only once the list is fully checked off; requires the explicit tap (no auto-trigger) since it mutates pantry data
- **Duplicate-sync guard:** shadcn `AlertDialog` ("This trip may have already been synced — sync again?") rather than a toast, since it blocks a data-mutating action
- **Live share indicator:** Small dot + label ("Live") in the shopping list header when viewing via a share link, reflecting Socket.IO connection state (connected/reconnecting)
- **Search and filter (pantry):** Debounced real-time search input combined with a category `Select`; both filters compose (AND, not OR)

## Design Considerations
- **Accessibility:** All status conveyed by color (expiration urgency, purchased/unpurchased) must also be conveyed by text or icon; interactive targets (checkboxes, delete buttons) sized for touch (minimum 44×44px); confirmation dialogs must trap focus and be dismissible via keyboard (Escape) per Radix defaults
- **Responsiveness:** Mobile-first layout for the Shopping List page specifically, since it's used mid-errand in-store with one hand; Pantry Inventory can use a denser, multi-column layout on tablet/desktop where users are more likely to be planning at a table
- **Offline tolerance (PWA):** Service worker caches the last-loaded pantry and shopping list views so a user can view (not necessarily mutate) their list in a low-connectivity store aisle; queued mutations sync and reconcile with a toast when connectivity returns
- **Installability:** PWA manifest and install prompt surfaced after a user's second visit, framed around the shopping-list use case ("Add PantryPal to your home screen for faster shopping trips")
- **Feedback latency:** Every mutating action (save, delete, sync, share) must produce a toast or visible state change within 300ms perceived response time via optimistic UI, even if the network round-trip takes longer

## Error States
| Scenario | User Sees | Recovery Action |
|----------|-----------|-----------------|
| Add/Edit pantry item missing required field | Inline red validation text under the field ("Name is required") on the Add/Edit sheet; form does not close | Correct the field and resubmit; sheet remains open with entered data preserved |
| Manual shopping item submitted without a name | Inline validation error on the Add Item form; item not added to list | Enter a name and resubmit |
| Delete pantry item requested | Confirmation `AlertDialog`: "Remove this item from your pantry?" | Confirm to delete, or Cancel to keep the item unchanged |
| Sync attempted when a prior sync already ran for this trip | `AlertDialog` warning: "It looks like this trip was already synced. Sync again?" | Confirm to proceed anyway, or Cancel to abort the sync |
| Shared list opened after full purchase + sync | Full-page "List Complete" state replacing the item list, with a link back to create a new list | Navigate to start a new shopping list |
| Network failure during save/sync | Toast: "Something went wrong — your change wasn't saved. Try again." | Retry the action; local optimistic UI reverts to last confirmed state if retry also fails |
| No pantry items match active search/filter | Empty state card: "No items found" with a "Clear filters" button | Tap "Clear filters" to reset search text and category selection |
