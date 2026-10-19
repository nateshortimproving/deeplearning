# PRD: Plant Watering Reminder App

## Problem Statement
Plant owners frequently forget to water their plants, or water them on a generic fixed schedule that doesn't match each plant's actual needs. The result is chronically underwatered or overwatered plants that wilt, develop root rot, or die — wasting money and discouraging people from keeping plants. Existing solutions are either manual calendar reminders (too rigid, ignore per-plant differences) or full-featured plant-care apps that are heavy and complicated for users who just want to know "when do I water this plant?"

## Proposed Solution
A lightweight mobile app where users add their plants, assign each one a watering frequency, and receive push notifications when a plant is due for watering. Users confirm each watering with a single tap, which resets that plant's schedule. The app stays out of the way: no accounts required to start, no social features, no plant encyclopedia — just reminders that adapt to each plant.

## Target Audience
- **Casual plant owners** — people with 1–10 houseplants who aren't horticultural experts and just need a nudge so plants don't die
- **Busy professionals** — users who intend to care for plants but lose track amid work/travel; need reminders that fit irregular schedules
- **New plant parents** — first-time owners unsure how often each plant type needs water; benefit from suggested defaults per plant species

## Functional Requirements
- The system shall allow a user to add a plant with a name, optional photo, optional species, and watering frequency (in days)
- The system shall provide a suggested default watering frequency when the user selects a known species from a predefined list
- The system shall send a local push notification on the day a plant is due for watering, at a user-configurable time of day
- The system shall let the user mark a plant as "watered" from the notification action or in-app, resetting that plant's next-due date
- The system shall display a list of all plants with their next watering due date, sorted by soonest due, with overdue plants visually highlighted
- The system shall support per-plant snooze ("remind me tomorrow") so a reminder can be deferred without marking the plant watered
- The system shall allow editing a plant's name, photo, species, and frequency, and deleting a plant
- The system shall persist all plant data and watering history locally on-device
- The system shall record a watering history log per plant (date watered, date due) viewable in the plant detail screen
- The system shall function fully offline; no network connection required for core features

## User Stories
- As a casual plant owner, I want to add each of my plants in under 30 seconds so that setup doesn't feel like a chore
- As a busy professional, I want a push notification when a plant is due so that I don't have to remember to check the app
- As a new plant parent, I want suggested watering frequencies for common species so that I don't have to guess
- As a plant owner, I want to tap "watered" directly from the notification so that logging a watering takes one second
- As a plant owner, I want to see which plants are overdue at a glance so that I can triage quickly
- As a plant owner with a variable schedule, I want to snooze a reminder so that I can water when I'm actually home
- As a plant owner, I want to see my watering history per plant so that I can spot whether I'm over- or under-watering

## Success Metrics
- ≥70% of users who add a plant still have the app installed and reminders enabled after 30 days
- ≥60% of watering reminders are confirmed ("watered" tapped) within 24 hours of firing
- Median time to add a new plant is under 45 seconds (measured via onboarding funnel/UX testing)
- Average number of days a plant remains overdue decreases by ≥50% compared to a self-reported baseline in onboarding survey
- <5% of users disable notifications within the first 14 days
- App supports at least 100 plants per user without degraded list rendering (<100ms scroll frame budget)

## Scope
### In Scope
- Single-user, on-device plant list with watering schedules
- Local push notifications with watered/snooze actions
- Predefined species list (top ~50 common houseplants) with default watering frequencies
- Plant photos via camera or photo library
- Per-plant watering history log
- iOS and Android support via a single cross-platform codebase
### Out of Scope
- Cloud sync, accounts, or multi-device support (deferred to v2)
- Shared/household plant lists or multi-user collaboration
- Automatic schedule adjustment based on season, humidity, or sensor data (e.g., smart-home/soil-sensor integrations)
- Plant disease diagnosis, care guides, fertilizing/misting/repotting reminders (deferred — evaluate after v1)
- Social features, plant collections marketplaces, or community content

## Assumptions
- Users opt in to push notifications during onboarding; the value proposition collapses without them, so the app should gate reminders on permission
- Users know their plants' common names well enough to pick from a predefined species list (free-text fallback exists otherwise)
- Watering frequency expressed in days is sufficient granularity; users do not need time-of-day-per-plant precision
- The app is a personal tool; no backend is required for v1

## Constraints
- Must work fully offline — all data and scheduling logic lives on-device (local notifications)
- Notification scheduling is limited by OS constraints (e.g., iOS caps pending local notifications at 64); schedule rolling reminders accordingly
- Must be buildable by a small team/solo developer; cross-platform framework (e.g., React Native/Flutter) preferred over two native codebases
- App must request notification permission per platform guidelines and degrade gracefully (in-app due list still works) if denied

## Dependencies
- OS local-notification APIs (iOS UNUserNotificationCenter / Android AlarmManager+WorkManager)
- A curated species→watering-frequency reference dataset (compiled in-house or licensed)
- Device camera/photo-library permissions for plant photos

## Open Questions
- Should reminders be one notification per plant, or a single daily digest notification listing all due plants? (Digest reduces notification fatigue; per-plant enables per-plant actions.)
- Should the app ask "did you water?" and auto-reschedule if unacknowledged, or leave plants simply marked overdue?
- Is a free-with-IAP or paid-upfront model desired, or is this a free utility?
- Do we need tablet/iPad layouts in v1?
