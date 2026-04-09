"""
Chapter prompt templates for DevBlueprint AI.
Each function returns the prompt string for that chapter given the user's answers.
"""

from app.models.blueprint import ProjectAnswers


def _context_block(answers: ProjectAnswers) -> str:
    return f"""
PROJECT CONTEXT:
- App Name: {answers.app_name}
- Description: {answers.app_description}
- Target Users: {answers.target_users}
- Core Features: {answers.core_features}
- Backend Stack: {answers.tech_stack_backend}
- Frontend Stack: {answers.tech_stack_frontend}
- Database: {answers.tech_stack_database}
- User Roles: {answers.user_roles}
- Expected Scale: {answers.expected_scale}
- Deployment Target: {answers.deployment_target}
""".strip()


def chapter_1_prompt(answers: ProjectAnswers) -> str:
    return f"""
You are DevBlueprint AI, an expert software architect and technical writer.
Generate Chapter 1 — Vision & Scope for the following project.

{_context_block(answers)}

Write a detailed, developer-ready Chapter 1 covering:
1. Idea Clarity — one-line pitch, problem being solved, who it's for, definition of done
2. Feature Breakdown — MVP core features, nice-to-have features, out-of-scope, priority matrix
3. Non-Functional Requirements — expected load, performance targets, availability SLA, security level
4. Page-Level Breakdown — all pages/screens, purpose of each, who can access, MVP priority
5. Competitor Inspiration — 3 reference applications, what to copy, what to do differently, differentiator statement

Be specific, actionable, and tailored to the exact project described. No generic filler.
Use tables where appropriate. Format sections with clear headings.
""".strip()


def chapter_2_prompt(answers: ProjectAnswers) -> str:
    return f"""
You are DevBlueprint AI, an expert software architect and technical writer.
Generate Chapter 2 — Functional Planning for the following project.

{_context_block(answers)}

Write a detailed, developer-ready Chapter 2 covering:
1. User Roles & Permissions — all roles defined, what each can/cannot do, permission matrix table
2. User Flows — happy path per major feature, alternate paths, role-based flows, guest vs logged-in
3. Edge Cases & Error States — validation rules, empty states, network failures, timeout handling, error message copy
4. Data Flow — what data enters the system, what gets transformed, stored, and returned
5. Business Rules — access control logic, notification triggers, state machines for key entities

Be specific and tailored to this exact project. Include tables and state diagrams as text.
""".strip()


def chapter_3_prompt(answers: ProjectAnswers) -> str:
    return f"""
You are DevBlueprint AI, an expert software architect and technical writer.
Generate Chapter 3 — Environment Setup for the following project.

{_context_block(answers)}

Write a complete, step-by-step Chapter 3 covering:
1. Local Machine Setup — OS prerequisites, runtime versions to install, package manager setup, PATH config
2. IDE & Plugins — recommended IDE, required plugins with install instructions, linting setup
3. Database Setup — account creation, cluster setup, connection string format, app config, test verification
4. Project Bootstrap — project generator config (Spring Initializr / Angular CLI / FastAPI), full dependency list with versions, config file templates (.env, application.yml, etc.)
5. Verify Setup Checklist — step-by-step verification, expected output per step, common errors and fixes

Every step must be explicit enough that a junior developer can follow without googling anything.
Stack being used: {answers.tech_stack_backend} backend, {answers.tech_stack_frontend} frontend, {answers.tech_stack_database} database.
""".strip()


def chapter_4_prompt(answers: ProjectAnswers) -> str:
    return f"""
You are DevBlueprint AI, an expert software architect and technical writer.
Generate Chapter 4 — Backend Blueprint for the following project.

{_context_block(answers)}

Write a complete, coding-agent-ready Chapter 4 covering:
1. Tech Stack Decision — chosen stack with justification, exact version numbers, key libraries and why
2. Folder Structure — full directory tree, responsibility of each layer, naming conventions
3. Database Schema — all collections/tables, fields with types and constraints, indexes, relationships, sample documents
4. Full API List — for every endpoint: URL, HTTP method, description, request body schema, response schema, error formats, auth required, rate limiting
5. Security — JWT flow, token expiry strategy, RBAC implementation, input validation, CORS config
6. Cross-Cutting Concerns — global exception handler, logging strategy, audit trail, standard response envelope

Be extremely specific. The output of this chapter should be paste-able into a coding agent prompt.
""".strip()


def chapter_5_prompt(answers: ProjectAnswers) -> str:
    return f"""
You are DevBlueprint AI, an expert software architect and technical writer.
Generate Chapter 5 — Frontend Blueprint for the following project.

{_context_block(answers)}

Write a complete, coding-agent-ready Chapter 5 covering:
1. Design System — color tokens, typography scale, spacing system, icon library, component library choice
2. Component Tree — all components listed with @Input/@Output, shared vs page-specific, component hierarchy
3. Pages & Routing — all routes (path, component, title), lazy loading strategy, route guards, 404 rules
4. State Management — state library choice, store structure, what lives in global store vs local component
5. API Integration — HTTP client setup, auth interceptor, error interceptor, loading state pattern, retry logic
6. UX Specifics — responsive breakpoints, animations, form validation UX, toast/notification system

Frontend stack: {answers.tech_stack_frontend}. Be specific enough that a coding agent can generate the full frontend in one pass.
""".strip()


def chapter_6_prompt(answers: ProjectAnswers) -> str:
    return f"""
You are DevBlueprint AI, an expert software architect and technical writer.
Generate Chapter 6 — Prompt Engineering Layer for the following project.

{_context_block(answers)}

Write Chapter 6 with ready-to-use prompts for coding agents. Include:
1. Backend Generation Prompt — a complete, paste-ready prompt for generating the entire backend (include schema, API list, folder structure, code style rules inline)
2. Frontend Generation Prompt — a complete, paste-ready prompt for generating the entire frontend (include design tokens, component list, API contracts, state structure)
3. Integration Prompt — step-by-step prompt for connecting frontend to backend (auth flow, interceptors, CORS)
4. Test Generation Prompt — prompt covering unit tests, integration tests, mocking strategy, test data setup
5. Iteration & Fix Prompt — how to re-prompt when output fails, what context to re-include, bug report template
6. Prompt Hygiene Rules — max context per prompt, chunking strategy, output format instructions, verification steps

Each prompt should be wrapped in a clear callout block and ready to copy-paste into Claude, Cursor, or Copilot.
""".strip()


def chapter_7_prompt(answers: ProjectAnswers) -> str:
    return f"""
You are DevBlueprint AI, an expert software architect and technical writer.
Generate Chapter 7 — Testing & QA for the following project.

{_context_block(answers)}

Write a complete testing plan covering:
1. Unit Testing — service layer coverage targets, repository layer, utility functions, test naming convention, mocking approach
2. Integration Testing — API contract tests per endpoint, database integration tests, auth flow tests, test containers setup
3. E2E Testing — tool choice with justification (Cypress/Playwright), critical user journeys to automate, setup/teardown, CI integration
4. Manual QA Checklist — feature-by-feature test checklist, cross-browser checks, mobile responsiveness, performance spot check
5. Edge Case Test Plan — boundary value tests, concurrent request tests, large data/pagination, auth expiry scenarios

Make the manual QA checklist a proper checkbox-style checklist. Be specific to this project's features.
""".strip()


def chapter_8_prompt(answers: ProjectAnswers) -> str:
    return f"""
You are DevBlueprint AI, an expert software architect and technical writer.
Generate Chapter 8 — Deploy & Launch for the following project.

{_context_block(answers)}

Write a complete deployment guide covering:
1. GitHub Setup — repository structure, branching strategy, .gitignore template, branch protection rules, README template
2. CI/CD Pipeline — pipeline config (GitHub Actions), build steps, test gates, deploy triggers, secrets management
3. Hosting Options — comparison of options relevant to this stack, recommendation with justification, free tier limits, scaling plan
4. Domain & SSL — where to buy domain, DNS configuration steps, SSL setup, subdomain strategy
5. Rollback Strategy — how to revert a failed deploy, database migration rollback, feature flag approach, zero-downtime deployment

Target deployment: {answers.deployment_target}. Be specific and include actual config file examples (GitHub Actions YAML, etc.).
""".strip()


def chapter_9_prompt(answers: ProjectAnswers) -> str:
    return f"""
You are DevBlueprint AI, an expert software architect and technical writer.
Generate Chapter 9 — Business & Data Layer for the following project.

{_context_block(answers)}

Write a business-readiness chapter covering:
1. Real-World Data Sources — relevant APIs and public datasets for this domain, free vs paid, data import strategy, freshness plan
2. Content / Topic Trees (if applicable) — hierarchy tree for the domain, depth levels, cross-links, coverage completeness
3. Market-Ready Suggestions — monetisation options with comparisons, pricing model ideas, growth levers (SEO, referral, integrations), launch checklist
4. Raw Material Sourcing — domain-specific sourcing guidance (suppliers, content providers, data feeds, compliance requirements)

Make this specific to the domain: {answers.app_description}. Include realistic pricing comparisons and actual named services/APIs.
""".strip()


def chapter_10_prompt(answers: ProjectAnswers) -> str:
    return f"""
You are DevBlueprint AI, an expert software architect and technical writer.
Generate Chapter 10 — Post-Launch & Maintenance for the following project.

{_context_block(answers)}

Write a complete post-launch plan covering:
1. Monitoring & Alerting — tool setup (Datadog/Azure Monitor/Grafana), key metrics to track, alert thresholds, on-call runbook
2. Logging Strategy — log levels and what to log at each, structured logging format, log retention policy, useful search queries
3. Update & Release Strategy — how to push updates safely (blue/green, canary), database migration process, semantic versioning, breaking change protocol
4. User Feedback Loop — bug report intake, feature request process, feedback → backlog pipeline, response SLA per issue type
5. Security Maintenance — dependency audit schedule, vulnerability scanning tools, secret rotation schedule, penetration test plan

Target deployment environment: {answers.deployment_target}. Be specific about tooling that works with this stack.
""".strip()


CHAPTER_PROMPTS = [
    chapter_1_prompt,
    chapter_2_prompt,
    chapter_3_prompt,
    chapter_4_prompt,
    chapter_5_prompt,
    chapter_6_prompt,
    chapter_7_prompt,
    chapter_8_prompt,
    chapter_9_prompt,
    chapter_10_prompt,
]

CHAPTER_TITLES = [
    "Vision & Scope",
    "Functional Planning",
    "Environment Setup",
    "Backend Blueprint",
    "Frontend Blueprint",
    "Prompt Engineering Layer",
    "Testing & QA",
    "Deploy & Launch",
    "Business & Data Layer",
    "Post-Launch & Maintenance",
]
