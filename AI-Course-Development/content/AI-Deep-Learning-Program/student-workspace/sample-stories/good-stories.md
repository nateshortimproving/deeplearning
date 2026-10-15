Generated Stories: Pantry & Shopping List
Source: sample-stories/pantry-inventory.md and sample-stories/shopping-list.md run together.

Epic 1: Pantry Inventory Management
As a home cook, I want to track the food items in my pantry so that I always know what I have, what is expiring soon, and what needs to be used before it goes bad.

Story PANTRY-001: Add Pantry Item Manually
User Story: As a home cook, I want to manually add a food item to my pantry so that I can keep an accurate record of what I have on hand.

Acceptance Criteria:

[positive] Given I am adding a new pantry item, when I enter all required information and confirm, then the item is saved and appears in my pantry inventory.
[positive] Given I have saved a new item, when I view the inventory list, then the item is grouped by category and the total item count increases by one.
[negative] Given I am adding a new pantry item, when I try to save without a required field, then the item is not saved and I see a clear validation message.
[edge_case] Given I add an item with the same name as an existing item, when I confirm the save, then the existing item quantity is updated instead of creating a duplicate.
Story PANTRY-002: Edit Existing Pantry Item
User Story: As a home cook, I want to edit an existing pantry item so that I can correct mistakes or update quantities after using some of an item.

Acceptance Criteria:

[positive] Given I am editing an existing pantry item, when I change a value and confirm, then the item is updated and I see a success confirmation.
[positive] Given I update an item's quantity, when the quantity reaches zero, then the item is marked as empty and visually distinguished.
[negative] Given I am editing an item, when I clear a required field and confirm, then the changes are not saved and I see a validation message.
[edge_case] Given I am editing an item, when I cancel the edit, then no changes are saved and I return to the inventory list.
Story PANTRY-003: Delete or Archive Pantry Item
User Story: As a home cook, I want to remove an item from my pantry so that my inventory reflects only what I actually have.

Acceptance Criteria:

[positive] Given I choose to remove a pantry item, when I confirm the removal, then the item is removed and the total item count decreases by one.
[negative] Given I open the remove confirmation, when I cancel, then the item remains in the inventory unchanged.
[edge_case] Given I remove the last item in a category, when the list refreshes, then the empty category is no longer displayed.
Story PANTRY-004: Expiration Alerts
User Story: As a home cook, I want to see which items are expiring soon so that I can prioritize using them before they go bad.

Acceptance Criteria:

[positive] Given I have items in my pantry, when I view the inventory, then each item shows a clear indicator of how soon it expires.
[positive] Given I have items expiring within 3 days, when I open the app, then I see a prominent alert that lists those items.
[negative] Given I have no items expiring within 7 days, when I open the app, then no expiration alert is shown.
[edge_case] Given an item's expiration date is today, when the inventory refreshes, then the item is shown as expiring today.
Story PANTRY-005: Filter and Search Inventory
User Story: As a home cook, I want to search and filter my pantry so that I can quickly find specific items without scrolling through the entire list.

Acceptance Criteria:

[positive] Given I am viewing my pantry, when I type in the search field, then only items matching the search text are shown.
[positive] Given I am viewing my pantry, when I select a category filter, then only items in that category are shown.
[edge_case] Given I apply search and category filters that match no items, when the list renders, then I see an empty state with a way to clear the filters.
Epic 2: Shopping List Generation
As a home cook, I want the app to automatically generate shopping lists from my pantry data so that I know exactly what to buy when items run low or run out.

Story SHOPPING-001: Auto-Generate Shopping List from Low Stock
User Story: As a home cook, I want the app to suggest items for my shopping list when they fall below a threshold so that I don't forget to restock essentials.

Acceptance Criteria:

[positive] Given I have pantry items below their low-stock threshold, when I view the shopping list, then those items appear in a suggestions section.
[positive] Given a suggested item, when I review it, then I see the quantity needed to reach the target stock level.
[negative] Given I have no items below their threshold, when I view the shopping list, then the suggestions section shows a message that no suggestions are needed.
[edge_case] Given an item is at exactly its threshold, when the list generates, then the item is not included in the suggestions.
Story SHOPPING-002: Manually Add Items to Shopping List
User Story: As a home cook, I want to manually add items to my shopping list so that I can include things I need that aren't tracked in my pantry.

Acceptance Criteria:

[positive] Given I want to add an item not in my pantry, when I enter the item details and confirm, then it appears in the manual section of the shopping list.
[negative] Given I try to add a manual item without a name, when I confirm, then the item is not saved and I see a validation message.
[edge_case] Given I add a manual item with the same name as an existing pantry item, when the list renders, then a hint suggests checking the pantry first.
Story SHOPPING-003: Check Off Purchased Items
User Story: As a home cook, I want to check off items as I purchase them so that I can track what is left to buy during a shopping trip.

Acceptance Criteria:

[positive] Given I am shopping, when I mark an item as purchased, then the item is shown as completed.
[positive] Given I have marked all items as purchased, when I view the list, then I see an option to add all purchased items to my pantry.
[negative] Given I accidentally mark an item as purchased, when I undo the action, then the item returns to its unpurchased state.
Story SHOPPING-004: Sync Purchased Items Back to Pantry
User Story: As a home cook, I want purchased shopping list items to update my pantry quantities so that my inventory stays accurate after a shopping trip without manual re-entry.

Acceptance Criteria:

[positive] Given I have purchased items that match existing pantry items, when I sync the shopping list to my pantry, then the matching pantry item quantities increase by the purchased amounts.
[positive] Given I have purchased items that do not match any pantry item, when I sync, then new pantry items are created with the purchased quantities.
[negative] Given I already synced a shopping trip, when I try to sync again, then I see a warning to confirm and avoid duplicate additions.
Story SHOPPING-005: Share Shopping List
User Story: As a home cook, I want to share my shopping list with a household member so that either of us can shop and check off items in real time.

Acceptance Criteria:

[positive] Given I want to share my shopping list, when I generate a share link, then the link is copied to my clipboard and I see a confirmation.
[positive] Given another user opens my shared list, when they view it, then they see the current items and purchase status.
[edge_case] Given a shared list has been fully purchased and synced, when a user opens the link, then they see a completion message instead of the item list.