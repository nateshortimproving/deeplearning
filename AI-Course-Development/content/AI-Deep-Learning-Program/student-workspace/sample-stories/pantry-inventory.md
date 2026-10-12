# Sample Epic: Pantry Inventory Management

## Epic Description
As a home cook, I want to track the food items in my pantry so that I always know what I have, what is expiring soon, and what needs to be used before it goes bad.

## Stories

### Story 1: Add Pantry Item Manually
As a user, I want to manually add a food item to my pantry so that I can keep an accurate record of what I have on hand.

**Acceptance Criteria:**
- Given I am on the pantry inventory page, when I click "Add Item", then a form opens with fields for name, quantity, unit, category, purchase date, and expiration date
- Given I fill out the add item form, when I submit with valid data, then the item is saved to my pantry and appears in the inventory list
- Given I am on the add item form, when I submit without a required field (name, quantity, expiration date), then the form shows validation errors and does not save
- Given I add a new item, when the inventory list reloads, then the new item is sorted into its category group and the total item count increments

### Story 2: Edit Existing Pantry Item
As a user, I want to edit an existing pantry item so that I can correct mistakes or update quantities after using some of an item.

**Acceptance Criteria:**
- Given I am viewing my pantry inventory, when I click "Edit" on an item, then a form opens pre-populated with the item's current values
- Given I am on the edit form, when I change a field and save, then the item is updated in the inventory list and a success toast appears
- Given I am on the edit form, when I change the quantity to zero, then the item is marked as "Empty" and displayed with a greyed-out style
- Given I am on the edit form, when I click "Cancel", then no changes are saved and I return to the inventory list

### Story 3: Delete or Archive Pantry Item
As a user, I want to remove an item from my pantry so that my inventory reflects only what I actually have.

**Acceptance Criteria:**
- Given I am viewing my pantry inventory, when I click "Delete" on an item, then a confirmation dialog appears asking me to confirm removal
- Given the delete confirmation dialog is open, when I click "Confirm", then the item is removed from the inventory and the total item count decrements
- Given the delete confirmation dialog is open, when I click "Cancel", then the item remains in the inventory unchanged
- Given I delete an item, when I view the inventory list, then the item no longer appears and the list re-renders without gaps

### Story 4: Expiration Alerts
As a user, I want to see which items are expiring soon so that I can prioritize using them before they go bad.

**Acceptance Criteria:**
- Given I have items in my pantry, when I view the inventory list, then each item shows a color-coded badge indicating expiration urgency (green > 7 days, yellow 3–7 days, red < 3 days, grey expired)
- Given I have items expiring within 3 days, when I open the app, then a banner at the top shows "N items expiring soon" with a link to filter them
- Given I click the expiration banner link, when the filtered view loads, then only items expiring within 3 days or already expired are shown
- Given I have no items expiring within 7 days, when I view the inventory, then no expiration banner is displayed

### Story 5: Filter and Search Inventory
As a user, I want to search and filter my pantry so that I can quickly find specific items without scrolling through the entire list.

**Acceptance Criteria:**
- Given I am on the pantry inventory page, when I type in the search bar, then the inventory list filters in real time to show only items whose name matches the search text
- Given I am on the pantry inventory page, when I select a category filter, then only items in that category are displayed
- Given I have active search text and a category filter, when both are applied, then only items matching both criteria are shown
- Given no items match the active filters, when the list renders, then an empty state message appears saying "No items found" with a button to clear filters