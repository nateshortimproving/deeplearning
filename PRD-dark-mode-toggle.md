# PRD: Dark Mode Toggle for Settings Screen

## Problem Statement
The app currently ships with a light theme only. Users in low-light environments (evening use, bedrooms, transit at night) experience eye strain and screen glare, and users who run their device in dark mode see the app as visually inconsistent with the rest of their system. Dark mode is now a baseline platform convention — its absence reads as a missing feature and generates recurring support feedback and app-store-review complaints.

## Proposed Solution
Add a theme control to the existing settings screen that lets the user choose between Light, Dark, and System (follow OS appearance). The selection applies immediately across the entire app without a restart, persists across launches, and "System" tracks the OS-level appearance setting in real time. Shipping this requires a complete dark color palette for all existing screens, implemented via design tokens rather than ad-hoc color overrides.

## Target Audience
- **Night-time / low-light users** — people who use the app in the evening or in dim environments and need reduced glare and eye strain
- **System-appearance users** — users who set their whole device to dark mode and expect every app to follow automatically
- **Accessibility-sensitive users** — users with light sensitivity or visual impairments for whom a bright UI is genuinely uncomfortable or unusable

## Functional Requirements
- (P0) The system shall display a "Theme" or "Appearance" control on the settings screen with three options: Light, Dark, and System
- (P0) The system shall apply the selected theme immediately to all screens, with no app restart required
- (P0) The system shall persist the user's theme selection locally and restore it on every app launch
- (P0) When set to "System," the system shall follow the OS appearance setting and update live if the OS appearance changes while the app is running or backgrounded
- (P0) The system shall render every existing screen in both palettes with text/background contrast meeting WCAG AA (4.5:1 for body text, 3:1 for large text and UI components)
- (P1) The system shall default new installs to "System" so the app matches OS appearance out of the box
- (P1) The system shall switch themes with a transition that does not flash, flicker, or leave unstyled frames
- (P2) The system should provide dark variants of branded imagery, illustrations, and status-bar styling where the light versions would clash with the dark palette

## User Stories
- As a night-time user, I want to switch the app to dark mode from settings so that using the app in a dark room doesn't strain my eyes
- As a system-appearance user, I want the app to follow my OS dark mode setting so that it matches the rest of my device without me configuring anything
- As a light-sensitive user, I want dark mode to persist between sessions so that I'm never surprised by a bright screen on launch
- As a user who changes my mind, I want the theme to update instantly when I toggle it so that I can preview and pick what I prefer
- As a user on an older device, I want dark mode to be readable so that text isn't washed out or low-contrast

## Success Metrics
- ≥25% of active users enable Dark or System-with-dark appearance within 60 days of release
- ≥95% of theme-preference changes persist correctly across app restarts (measured via preference-integrity logging or QA regression)
- Theme switch applies in <300ms on median-spec devices with no dropped frames perceptible in UI testing
- Zero accessibility regressions: automated + manual contrast audit passes WCAG AA on 100% of screens before release
- No increase in crash rate (<0.1pp delta) or readability-related support tickets after rollout
- App-store-review mentions of "dark mode" complaint volume trends to zero within 90 days

## Scope
### In Scope
- Theme selector (Light / Dark / System) on the existing settings screen
- Complete dark color palette applied to all current screens and components
- Local persistence of the user's selection
- Live response to OS appearance changes while "System" is selected
- Dark variants of status-bar styling and key branded assets

### Out of Scope
- Scheduled or automatic dark mode (e.g., sunset-to-sunrise, custom time schedule) — deferred; "System" already covers this for most users
- Per-screen or per-feature theme overrides (theme is app-global)
- Custom themes, accent-color pickers, or additional palettes beyond light/dark
- Dark mode for surfaces outside the app shell: home-screen widgets, notifications, app icon variants, website/email templates
- Forcing a dark theme on web views of third-party content that renders its own colors

## Assumptions
- The app already has a settings screen where a new row/section can be added without structural redesign
- The app's colors are (or will be refactored to be) driven by a design-token/theme layer rather than hard-coded hex values scattered through views
- The app's minimum supported OS versions expose a system appearance API (iOS 13+/Android 10+ or equivalent)
- A dark palette that preserves brand identity can be defined by design without a full rebrand

## Constraints
- Must meet WCAG AA contrast in both themes; pure-black vs. pure-white choices must be deliberate for OLED/contrast trade-offs
- The toggle must not require an app restart or re-authentication
- Third-party components/screens (e.g., payment sheets, SDK-rendered views) must be audited; only what we control can be themed, and unthemeable surfaces must not break visually
- Effort is bounded by auditing every existing screen — this is a broad but shallow change, not a new subsystem

## Dependencies
- A complete, approved dark design-token palette from the design team
- OS appearance APIs (iOS `UITraitCollection`/`UIUserInterfaceStyle`, Android `AppCompatDelegate`/`uiMode`, or the cross-platform equivalent)
- Settings-persistence mechanism already used by the app for user preferences
- Third-party SDK surfaces used in-app must expose a dark/theme parameter or be wrapped

## Open Questions
- Should the default for existing users (who never had a choice) be "System" or "Light" to preserve their current experience? (Recommended: "System" for new installs, "Light" migration for existing installs is defensible either way.)
- Do any screens rely on third-party SDK views we cannot theme, and do we accept a mixed appearance there?
- Should brand photography/illustrations get true dark variants, or is a neutral dimming treatment acceptable for v1?
- Does this need a server-side/remote flag for staged rollout, or ship to 100% at release?
