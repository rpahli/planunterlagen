# Tasks: Static Site for Markdown Files on GitHub Pages

**Input**: Design documents from `/specs/001-markdown-site-pages/`
**Prerequisites**: `plan.md` (required), `spec.md` (required for user stories), `research.md`, `data-model.md`, `contracts/`

**Tests**: No strict TDD-first test tasks were requested in `spec.md`; verification is implemented through strict build/link/smoke validation tasks inside each story.

**Organization**: Tasks are grouped by user story so each story can be implemented and validated independently.

## Format: `[ID] [P?] [Story] Description`

- **[P]**: Can run in parallel (different files, no dependencies)
- **[Story]**: Which user story this task belongs to (`US1`, `US2`, `US3`)
- Include exact file paths in each task description

## Phase 1: Setup (Shared Infrastructure)

**Purpose**: Initialize MkDocs/Material project scaffolding and deployment files.

- [X] T001 Create docs dependency manifest in `requirements-docs.txt`
- [X] T002 [P] Create initial docs skeleton in `docs/index.md`
- [X] T003 [P] Create custom stylesheet scaffold in `docs/stylesheets/extra.css`
- [X] T004 Create baseline MkDocs configuration in `mkdocs.yml`
- [X] T005 Create GitHub Pages workflow scaffold in `.github/workflows/docs-pages.yml`

---

## Phase 2: Foundational (Blocking Prerequisites)

**Purpose**: Establish shared publishing rules, validation gates, and lifecycle policies required by all stories.

**CRITICAL**: Complete this phase before starting user story implementation.

- [X] T006 Define include/exclude publication scope policy in `docs/maintenance/publishing-scope.md`
- [X] T007 Configure strict validation defaults in `mkdocs.yml`
- [X] T008 [P] Define link-check policy and thresholds in `tests/docs/link-policy.md`
- [X] T009 Add CI link-check workflow in `.github/workflows/docs-link-check.yml`
- [X] T010 Define URL lifecycle and depublication policy in `docs/maintenance/url-lifecycle.md`
- [X] T011 Document maintainer roles and ownership in `docs/maintenance/publishing-runbook.md`

**Checkpoint**: Foundation complete; user stories can proceed.

---

## Phase 3: User Story 1 - Publish Markdown as a Browsable Website (Priority: P1) 🎯 MVP

**Goal**: Deliver a live, navigable GitHub Pages site generated from repository Markdown.

**Independent Test**: Trigger the Pages workflow, open the public site URL, and verify visitors can navigate and read published pages without repository access.

### Implementation for User Story 1

- [X] T012 [US1] Add initial public landing content in `docs/index.md`
- [X] T013 [P] [US1] Create first navigation content page in `docs/guide/getting-started.md`
- [X] T014 [P] [US1] Create second navigation content page in `docs/guide/publishing-overview.md`
- [X] T015 [US1] Configure explicit site navigation and Material theme settings in `mkdocs.yml`
- [X] T016 [US1] Implement baseline branding variables and readability styles in `docs/stylesheets/extra.css`
- [X] T017 [US1] Complete build-and-deploy job definitions in `.github/workflows/docs-pages.yml`
- [X] T018 [US1] Add local publish/preview instructions for maintainers in `README.md`

**Checkpoint**: User Story 1 is independently deployable and browsable.

---

## Phase 4: User Story 2 - Keep Website in Sync with Content Updates (Priority: P2)

**Goal**: Ensure Markdown updates, additions, and lifecycle changes are reflected reliably and quickly on the live site.

**Independent Test**: Update one existing page and add one new page, run CI, and verify both changes appear on the published site within the expected republish window.

### Implementation for User Story 2

- [X] T019 [US2] Add content update checklist for maintainers in `docs/maintenance/content-update-checklist.md`
- [X] T020 [P] [US2] Add navigation-sync checker script in `scripts/docs/check_nav_sync.py`
- [X] T021 [US2] Integrate navigation-sync checker into `.github/workflows/docs-pages.yml`
- [X] T022 [P] [US2] Add redirects plugin dependency in `requirements-docs.txt`
- [X] T023 [US2] Configure redirect rules support and initial mappings in `mkdocs.yml`
- [X] T024 [US2] Document rename/move/delete handling process in `docs/maintenance/content-lifecycle.md`

**Checkpoint**: User Story 2 content sync behavior is independently verifiable.

---

## Phase 5: User Story 3 - Choose a Fit-for-Purpose Publishing Approach (Priority: P3)

**Goal**: Provide an explicit recommendation record with alternatives, rationale, prerequisites, and ownership expectations.

**Independent Test**: Review the decision artifact and confirm it captures criteria, alternatives, chosen approach, prerequisites, ownership, and approval fields.

### Implementation for User Story 3

- [X] T025 [US3] Create decision record for publishing approach in `docs/decisions/001-publishing-approach.md`
- [X] T026 [P] [US3] Create prerequisites and responsibilities guide in `docs/maintenance/publishing-prerequisites.md`
- [X] T027 [P] [US3] Create owner sign-off template in `docs/decisions/decision-signoff-template.md`
- [X] T028 [US3] Add decision and governance pages to site navigation in `mkdocs.yml`
- [X] T029 [US3] Link recommendation and maintainer guidance from home page in `docs/index.md`

**Checkpoint**: User Story 3 recommendation package is independently reviewable.

---

## Phase 6: Polish & Cross-Cutting Concerns

**Purpose**: Final consistency pass across all stories.

- [X] T030 [P] Add documentation troubleshooting guide in `docs/maintenance/troubleshooting.md`
- [X] T031 Align quickstart commands with implemented workflow in `specs/001-markdown-site-pages/quickstart.md`
- [X] T032 Record final smoke-check execution plan in `tests/docs/smoke-check-plan.md`
- [X] T033 Run strict build and capture maintainer verification notes in `docs/maintenance/publishing-runbook.md`

---

## Dependencies & Execution Order

### Phase Dependencies

- **Phase 1 (Setup)**: No dependencies.
- **Phase 2 (Foundational)**: Depends on Phase 1; blocks all user stories.
- **Phase 3 (US1)**: Depends on Phase 2; MVP release slice.
- **Phase 4 (US2)**: Depends on Phase 2 and integrates with US1 publication workflow.
- **Phase 5 (US3)**: Depends on Phase 2; can run in parallel with US2 after foundation.
- **Phase 6 (Polish)**: Depends on completion of selected user stories.

### User Story Dependencies

- **US1 (P1)**: Starts immediately after Foundational phase.
- **US2 (P2)**: Starts after Foundational; relies on deployed pipeline shape from US1.
- **US3 (P3)**: Starts after Foundational; independent from code-path changes in US2.

### Within Each User Story

- Establish or update content/schema files before wiring workflow automation.
- Configure CI/deploy integration after the relevant docs/config artifacts exist.
- Complete each story checkpoint before marking the story done.

### Parallel Opportunities

- Setup: `T002` and `T003` can run in parallel.
- Foundational: `T008` can run in parallel with `T009` and `T010` after `T007`.
- US1: `T013` and `T014` can run in parallel before `T015`.
- US2: `T020` and `T022` can run in parallel before `T021`/`T023`.
- US3: `T026` and `T027` can run in parallel before `T028`.

---

## Parallel Example: User Story 1

```bash
# Parallel content authoring
Task: "T013 [US1] Create first navigation content page in docs/guide/getting-started.md"
Task: "T014 [US1] Create second navigation content page in docs/guide/publishing-overview.md"

# Then integrate navigation/deploy
Task: "T015 [US1] Configure explicit site navigation and Material theme settings in mkdocs.yml"
Task: "T017 [US1] Complete build-and-deploy job definitions in .github/workflows/docs-pages.yml"
```

## Parallel Example: User Story 2

```bash
# Parallel sync foundations
Task: "T020 [US2] Add navigation-sync checker script in scripts/docs/check_nav_sync.py"
Task: "T022 [US2] Add redirects plugin dependency in requirements-docs.txt"

# Then wire into pipeline/config
Task: "T021 [US2] Integrate navigation-sync checker into .github/workflows/docs-pages.yml"
Task: "T023 [US2] Configure redirect rules support and initial mappings in mkdocs.yml"
```

## Parallel Example: User Story 3

```bash
# Parallel governance docs
Task: "T026 [US3] Create prerequisites and responsibilities guide in docs/maintenance/publishing-prerequisites.md"
Task: "T027 [US3] Create owner sign-off template in docs/decisions/decision-signoff-template.md"

# Then publish in IA
Task: "T028 [US3] Add decision and governance pages to site navigation in mkdocs.yml"
```

---

## Implementation Strategy

### MVP First (User Story 1 Only)

1. Complete Phase 1 (Setup).
2. Complete Phase 2 (Foundational).
3. Complete Phase 3 (US1).
4. Validate US1 independently by deploying and browsing the live site.

### Incremental Delivery

1. Deliver US1 as MVP publication baseline.
2. Add US2 for synchronization, redirects, and lifecycle reliability.
3. Add US3 decision/governance artifacts for long-term maintainability.
4. Finish with Phase 6 polish and final validation evidence.

### Suggested MVP Scope

- **Recommended MVP**: Through `T018` (Phase 3 / User Story 1).
