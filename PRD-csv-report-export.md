# PRD: CSV Report Export

## Problem Statement
Users can view reports in the product but have no way to get the underlying data out for their own workflows. They need CSV exports to join report data with other systems (Excel, BI tools, CRM imports), share results with stakeholders who lack product access, and keep offline records for audits. Today they resort to manual copy-paste or screenshots, which is error-prone, loses data fidelity, and generates recurring feature requests to support.

## Proposed Solution
Add an "Export to CSV" action to every report view that downloads a standards-compliant CSV of the report's data exactly as filtered and configured on screen. Exports complete inline for typical report sizes; oversized exports are rejected with a clear message rather than silently truncating. The CSV carries a header row, UTF-8 encoding, and RFC 4180 escaping so it opens cleanly in Excel, Google Sheets, and data pipelines.

## Target Audience
- **Analysts and power users** — pull report data into Excel/Sheets or BI tools for further analysis the product doesn't support
- **Managers and stakeholders** — share report results with people who don't have product accounts
- **Operations and compliance users** — keep point-in-time records of report output for audits and reconciliations

## Functional Requirements
- (P0) The system shall display an "Export to CSV" action on every report view, disabled or hidden only when the user lacks permission to view that report
- (P0) The exported CSV shall contain exactly the rows, columns, filters, and date range currently applied to the report on screen — no hidden or additional fields
- (P0) The CSV shall include a header row matching the column names shown in the report UI
- (P0) The CSV shall be UTF-8 encoded (with BOM for Excel compatibility) and follow RFC 4180 escaping rules for commas, quotes, and newlines in field values
- (P0) The download filename shall identify the report and export date, e.g. `monthly-usage-report-2026-10-19.csv`
- (P0) The export shall include only data the requesting user is authorized to view under existing report permissions
- (P1) When a report is empty (zero rows under current filters), the system shall still export a CSV containing only the header row rather than erroring
- (P1) Exports exceeding a defined row limit (e.g., 100k rows) shall be rejected before generation with a message telling the user to narrow their filters
- (P1) The system shall log export events (user, report, row count, timestamp) for audit and usage analytics
- (P2) The system should format dates, numbers, and booleans in the CSV consistently with the report UI's display formats unless a column is inherently machine-typed (e.g., IDs, ISO timestamps)

## User Stories
- As an analyst, I want to export a filtered report to CSV so that I can combine it with other data in Excel without manual copy-paste
- As a manager, I want to download a report as CSV so that I can share it with stakeholders who don't have product accounts
- As a compliance user, I want export files to capture exactly what was on screen so that my audit record is faithful to what was reviewed
- As a user on a huge dataset, I want to be told upfront that my export is too large so that I can narrow the date range instead of waiting for a failed download
- As an admin, I want export activity logged so that I can trace who exported sensitive report data and when

## Success Metrics
- ≥30% of active report viewers use CSV export at least once within 60 days of release
- ≥99% of initiated exports complete successfully (no server error, corrupt file, or truncated output)
- Median export generation-to-download-start time under 5 seconds for reports up to 10k rows
- Zero data-integrity complaints: exported rows match on-screen report rows 1:1 in QA sampling across all report types
- Zero permission-escalation incidents: no export contains data the requester couldn't view in the UI
- Measurable decline in "export/download data" feature requests to support within 90 days

## Scope
### In Scope
- Per-report "Export to CSV" action on all existing report views
- CSV output reflecting the report's current filters, columns, and date range
- Header row, UTF-8 encoding with BOM, RFC 4180 escaping, descriptive filenames
- Row-limit guard with user-facing error messaging
- Audit logging of export events

### Out of Scope
- Other export formats (XLSX, PDF, JSON, TSV) — deferred; CSV covers the dominant use case
- Scheduled or recurring exports, or export delivery via email — separate initiative
- Async/background export pipeline for datasets above the row limit — v2 if the limit proves too tight
- Bulk export of multiple reports in one action
- A public export API for programmatic access
- Column selection or field remapping at export time (export mirrors the on-screen configuration)

## Assumptions
- Reports are rendered from a queryable data layer where the same query can be re-run server-side for export
- A permission model already governs report visibility and can be applied to exports
- Users understand CSV as a format and have a tool (Excel, Sheets) to open it
- Report volumes fit within the row limit for the majority of use cases

## Constraints
- Export must reflect the report's current on-screen state; generating CSV from a different query path than the UI risks divergence and is disallowed
- Large exports must not degrade report-viewing performance for other users (generation must be bounded in memory/time)
- Exported files are untracked once downloaded — sensitive-data handling obligations (e.g., GDPR) still apply, so logging and permission checks are mandatory
- CSV has no typing or formatting; ambiguous fields (dates, leading-zero IDs) must be formatted so common spreadsheet tools don't corrupt them

## Dependencies
- The report data/query layer must expose a way to execute the same query the UI used, streamed or paged for CSV serialization
- Existing auth/permission service for per-row or per-report access checks
- Audit/event logging infrastructure for export tracking
- Frontend capability to trigger a file download (or streamed response) from the report view

## Open Questions
- What row limit balances usability vs. load — is 100k rows right, and should it differ per report type?
- Should exports include a metadata header (report name, filters, export timestamp) above the column headers, or stay strictly tabular for pipeline ingestion?
- Do date/number fields need a "raw value" mode for power users vs. display-formatted values for stakeholders?
- Is an async "email me the file" fallback needed for exports near the limit, or is rejecting with narrower filters acceptable for v1?
