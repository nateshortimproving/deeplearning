[Definitions]
• IMPLEMENTATION.md: The implementation summary — which plan tasks were implemented, assumptions made, deviations from the plan, and test file locations.
• Task Traceability: Every plan task maps to a code change in at least one of its files_affected.
• AC Coverage: Every acceptance_criteria_refs entry in the plan is exercised by tests (positive, negative, edge).
• Scope Discipline: Only plan-referenced tasks and AC are implemented; nothing from the raw story outside the plan.

EC 1: Task traceability — the summary lists which plan task ids were implemented.
EC 2: AC coverage — the summary references the acceptance criteria it satisfies.
EC 3: Testing — the summary lists at least one test file exercising the implemented behavior.
EC 4: Architectural alignment — code follows the declared stack (Fastify, Prisma, TypeScript; React + hooks for frontend). [judge]
EC 5: IMPLEMENTATION.md exists with Tasks Implemented, Assumptions, Deviations, and Test Files sections — each non-empty or an explicit "None".
EC 6: Scope discipline — nothing is implemented beyond the plan's task and AC references. [judge]
