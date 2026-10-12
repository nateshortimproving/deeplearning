# Sample Epic: Shopping List Generation

## Epic Description
As a home cook, I want the app to automatically generate shopping lists from my pantry data so that I know exactly what to buy when items run low or run out.

## Stories

### Story 1: Auto-Generate Shopping List from Low Stock
As a user, I want the app to suggest items for my shopping list when they fall below a threshold so that I don't forget to restock essentials.

**Acceptance Criteria:**
- Given I have pantry items with quantity below their defined low-stock threshold, when I navigate to the shopping list page, then those items appear in a "Suggested" section
- Given I have pantry items at zero quantity, when I view the shopping list, then those items appear in the "Suggested" section with a badge labeled "Out of stock"
- Given I have no items below their low-stock threshold, when I view the shopping list, then the "Suggested" section shows "No suggestions — your pantry is well stocked"
- Given an item is suggested, when I view its entry, then the suggested quantity to buy equals the difference between the target stock level and current quantity

### Story 2: Manually Add Items to Shopping List
As a user, I want to manually add items to my shopping list so that I can include things I need that aren't tracked in my pantry.

**Acceptance Criteria:**
- Given I am on the shopping list page, when I click "Add Item", then a form opens with fields for name, quantity, unit, and optional category
- Given I fill out the add item form, when I submit with valid data, then the item appears in the "Manual" section of the shopping list
- Given I am on the add item form, when I submit without a name, then the form shows a validation error and does not save
- Given I add a manual item that matches an existing pantry item name, when the list renders, then a hint appears suggesting I check my pantry first

### Story 3: Check Off Purchased Items
As a user, I want to check off items as I purchase them so that I can track what is left to buy during a shopping trip.

**Acceptance Criteria:**
- Given I have items on my shopping list, when I tap the checkbox next to an item, then the item is marked as purchased with a strikethrough style
- Given I have checked off all items, when I view the shopping list, then a "Shopping Complete" banner appears with a button to "Add All to Pantry"
- Given I click "Add All to Pantry", when the action completes, then all purchased items are added to my pantry inventory with today's purchase date and the shopping list is cleared
- Given I accidentally checked an item, when I tap the checkbox again, then the item is unchecked and returned to the unpurchased state

### Story 4: Sync Purchased Items Back to Pantry
As a user, I want purchased shopping list items to update my pantry quantities so that my inventory stays accurate after a shopping trip without manual re-entry.

**Acceptance Criteria:**
- Given a purchased item matches an existing pantry item by name, when I sync purchases to pantry, then the pantry item's quantity is increased by the purchased amount
- Given a purchased item does not match any existing pantry item, when I sync purchases to pantry, then a new pantry item is created with the purchased quantity and a default category of "Uncategorized"
- Given multiple purchased items are synced, when the sync completes, then a summary toast appears showing "N items added to pantry" and the inventory reflects updated quantities
- Given a sync has already been performed for a shopping trip, when I attempt to sync again, then a warning appears asking me to confirm to avoid duplicate additions

### Story 5: Share Shopping List
As a user, I want to share my shopping list with a household member so that either of us can shop and check off items in real time.

**Acceptance Criteria:**
- Given I am on the shopping list page, when I click "Share", then a shareable link is generated and copied to my clipboard with a toast confirming the copy
- Given I have shared a shopping list link, when another user opens it, then they see the current shopping list with all items and their purchased status
- Given two users are viewing the same shared list, when one user checks off an item, then the other user sees the item marked as purchased within 3 seconds
- Given a shared list has been fully purchased and synced, when a user opens the link, then they see a "List Complete" message instead of the item list