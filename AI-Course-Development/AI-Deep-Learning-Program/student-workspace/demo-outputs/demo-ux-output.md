# UX Design Guidance: Pantry Tracker PWA

> **Demo output** — produced by running the `create-ux` skill (RT-only stub, no Context or Constraints). This is intentionally generic. The guidance lacks user research, accessibility constraints, brand-specific design patterns, and platform guidelines that Context and Constraints would provide.

---

## User Flows

### Flow 1: First-Time Adding Items
1. User installs or opens the Pantry Tracker PWA
2. User sees an empty pantry state with a prominent "Add your first item" call to action
3. User taps "Add Item"
4. User enters item name, quantity, category, and expiration date manually — or scans a barcode
5. User saves the item
6. Item appears in the pantry list; user is prompted to add more items

### Flow 2: Checking What's Expiring
1. User opens the app and lands on the pantry list view
2. Items are sorted by expiration date, with soon-to-expire items highlighted at the top
3. User taps an expiring item to see details (quantity, date, category)
4. User marks the item as used, removes it, or dismisses the alert
5. The pantry list updates to reflect the change

### Flow 3: Generating a Shopping List
1. User taps the "Shopping List" tab or icon
2. App auto-generates a list from depleted items, low-stock items, and items the user has marked as "need to buy"
3. User reviews the list, adds manual entries, or removes items they don't need
4. User checks off items while shopping
5. Checked-off items can be quickly added back to the pantry with a new expiration date

### Flow 4: Scanning a Barcode
1. User taps "Scan" from the add-item flow or the main pantry view
2. Camera opens within the PWA
3. User points the camera at a product barcode
4. App looks up the product name and category from the barcode
5. User confirms or edits the pre-filled details and enters an expiration date
6. Item is saved to the pantry

## Key Interaction Patterns

- **Swipe actions** on pantry list items — swipe left to remove, swipe right to mark as used
- **Bottom navigation bar** with three tabs: Pantry, Shopping List, Add (center FAB-style button)
- **Color-coded expiration badges** — green (>7 days), yellow (3–7 days), red (<3 days or expired)
- **Optimistic UI updates** — item removal and edits reflect immediately, with background sync to the server
- **Pull-to-refresh** on the pantry list to force a sync with the backend
- **Toast notifications** when an item is added, removed, or synced

## Design Considerations

- **Mobile-first layout:** The app is designed primarily for phone usage in the kitchen. Lists and forms should be comfortably usable one-handed.
- **Offline-first PWA:** The UI must function fully offline. Changes are queued and synced when connectivity returns. A visible offline indicator should appear in the header when disconnected.
- **ShadCN component usage:** Use shadcn/ui Card components for item display, Badge components for expiration status, Sheet components for the add/edit form, and Dialog components for confirmations.
- **Quick entry:** The add-item flow should require minimal taps. Barcode scan and common-item autocomplete reduce friction.
- **Empty/edge states:** When the pantry is empty, show an onboarding prompt. When a barcode lookup fails, fall back gracefully to manual entry without blocking the user.
- **Installability:** The app should prompt users to "Add to Home Screen" after their first successful item add, using a custom install prompt rather than the browser's default.

## Likely User Decision Points and Error Points

### Decision Points
- **Manual entry vs. barcode scan:** Users may not know which approach to use. The add flow should present both options equally without requiring the user to commit to one path upfront.
- **When to mark an item as "used" vs. "remove":** Users may be unsure whether "used" means "I ate it" or "remove from list." Clear labels and brief helper text should distinguish these actions.
- **Shopping list trust:** Users may not trust the auto-generated shopping list if it includes items they already have. The list should show why each item was suggested (e.g., "Out of stock," "Expires soon, replace?").

### Error Points
- **Barcode lookup failure:** If the barcode API returns no match, the user should be seamlessly dropped into manual entry with the barcode pre-filled, not shown an error screen.
- **Sync conflicts:** If the user edits the pantry on two devices while offline, conflicts may arise when both sync. A simple last-write-wins policy with a notification is proposed for the initial version.
- **Camera permission denied:** If the user denies camera access for barcode scanning, the scan option should be disabled with an explanation and a link to browser settings, while manual entry remains fully available.
- **Offline add with failed sync:** If a user adds items offline and the sync later fails, the items should remain visible in the local pantry with a "sync pending" indicator, not disappear.