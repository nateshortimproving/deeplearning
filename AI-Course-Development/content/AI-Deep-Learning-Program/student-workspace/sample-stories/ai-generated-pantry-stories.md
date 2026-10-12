# Sample Epic: AI-Generated Pantry Stories (AI-Generated Without Care)

> **Demo file** — produced by asking an AI to "write epics and stories for a pantry tracker app" with no Context (WHY), no Constraints (HOW), and no Evaluation Criteria. The output sounds polished but has real problems: acceptance criteria describe implementation detail, epics are too large and poorly scoped, edge cases are missing, and some AC are untestable. Use this as the "AI-generated-without-care" example in the good/bad/AI-generated demo in Session 1.

---

## Epic 1: Comprehensive Pantry Management System

### Story 1.1: Add Pantry Item

As a user, I want to add items to my pantry so that I can maintain an accurate inventory of all my food items.

**Acceptance Criteria:**
- Given the user is on the dashboard, when they click the "Add Item" button in the top navigation bar, then a modal dialog opens with a form containing input fields for item name, quantity, unit of measure, category, purchase date, expiration date, and optional notes
- Given the modal is open, when the user fills in all required fields and clicks "Save", then the system inserts a new record into the `pantry_items` table in the PostgreSQL database with a UUID primary key, created_at timestamp, and the user's ID from the JWT token
- Given the form is submitted, when validation passes, then the backend API returns a 201 Created status code with the new item object in the response body and the frontend updates the Redux store to include the new item in the sorted inventory list
- Given the user clicks "Cancel", when the modal closes, then no API call is made and the form state is reset

### Story 1.2: View Pantry Dashboard

As a user, I want to see a dashboard of all my pantry items so that I have a comprehensive overview of my inventory at a glance.

**Acceptance Criteria:**
- Given the user navigates to the home route `/`, when the Dashboard component mounts, then the system fetches all pantry items from the API and displays them in a responsive grid layout with category-based filtering tabs
- Given the dashboard has loaded, when the user views the grid, then each card shows the item name, quantity with unit, expiration date with color-coded urgency badge, and a thumbnail image if available
- Given there are more than 20 items, when the user scrolls down, then infinite loading triggers a lazy fetch of the next 20 items from the paginated API endpoint

### Story 1.3: Comprehensive Expiration Management

As a user, I want the system to automatically handle expiration tracking so that I never miss an expiring item.

**Acceptance Criteria:**
- Given the system is running, when a cron job executes at midnight UTC daily, then the backend scans all pantry items and flags any item with an expiration date within 3 days
- Given flagged items exist, when the user opens the app, then push notifications are sent via the Firebase Cloud Messaging API to the user's registered device tokens
- Given an item has expired, when the user views it, then it is displayed with a red overlay and a "Mark as Discarded" action button
- Given the user clicks "Mark as Discarded", when the item is removed from active inventory, then it is archived to the `discarded_items` table with a timestamp for waste tracking analytics

### Story 1.4: Multi-User Household Management

As a user, I want to share my pantry with my family members so that we can all stay in sync.

**Acceptance Criteria:**
- Given the account owner, when they navigate to Settings > Household, then they can invite up to 5 additional users via email with a join link
- Given a household exists, when any member adds, edits, or removes an item, then all other members see the change reflected within 5 seconds via WebSocket connection
- Given household members exist, when viewing the pantry, then each item shows which member last modified it with their avatar and timestamp

---

## Epic 2: Intelligent Shopping List Generation

### Story 2.1: AI-Powered Shopping List

As a user, I want the system to generate a shopping list using AI so that I always know what to buy.

**Acceptance Criteria:**
- Given the pantry has items below threshold, when the user clicks "Generate Shopping List", then the system calls the OpenAI GPT-4 API with the current pantry state and receives a structured JSON shopping list response
- Given the AI response, when the shopping list is created, then it is saved to the `shopping_lists` table with a reference to the generating pantry items and a confidence score
- Given the user reviews the list, when they disagree with a suggestion, then they can swipe to remove it and the system logs the rejection for future AI model fine-tuning

### Story 2.2: Smart Category Grouping

As a user, I want my shopping list grouped by grocery store aisle so that I can shop efficiently.

**Acceptance Criteria:**
- Given a shopping list exists, when the user views it, then items are grouped by category matching common grocery store layouts (produce, dairy, bakery, frozen, pantry, household)
- Given the user is at the store, when they toggle "Shopping Mode", then the list switches to a checklist view with items sorted by aisle order and a running total of estimated cost