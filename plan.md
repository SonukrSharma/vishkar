# Vishkar — MVP Plan

> Build the right thing, in the right order. Each MVP ships something real.

---

## Stack Decision

| Layer | Choice | Why |
|---|---|---|
| Backend / Agent | Python + FastAPI | Native AI ecosystem, mature Anthropic SDK, async streaming support |
| LLM | Claude API (`claude-sonnet-4-6`) | Best long-form structured generation, excellent instruction following |
| Document Generation | `python-docx` | Industry standard for `.docx`, well-documented |
| Frontend | Next.js (React) | SSR for SEO, file-based routing, Vercel-ready, shadcn/ui for components |
| Database | MongoDB (Atlas) | Session + blueprint storage, flexible schema |
| Hosting | TBD | Decided at MVP 5 |

> Spring AI is a future consideration for a Java rewrite if enterprise adoption requires it. Not now.

---

## MVP 1 — Core Engine (CLI, No UI)

**Goal:** Prove the core loop works. Question → LLM → `.docx` output.

**What it includes:**
- FastAPI project scaffolded and running locally
- Static question list (10 questions, no branching yet)
- Collect answers via CLI / simple API call (Postman-testable)
- Claude API integration — one call per chapter
- All 10 chapters generated sequentially
- Basic `.docx` assembled with `python-docx` (text only, no fancy formatting)
- Download endpoint returns the `.docx` file

**What it excludes:**
- Frontend UI
- MongoDB (flat JSON files for session storage)
- Adaptive question logic
- PDF output
- Diagrams or images in the doc
- Authentication

**Success criteria:**
- Given answers to 10 questions, the system produces a downloadable `.docx` blueprint with all 10 chapters populated with relevant, useful content.

---

## MVP 2 — Quality & Formatting

**Goal:** Make the output document actually good — something you'd be proud to show a client.

**What it includes:**
- Improved prompt engineering per chapter (iterate on MVP 1 output quality)
- Professional `.docx` formatting:
  - Cover page (app name, date, stack)
  - Table of contents
  - Chapter headings and section structure
  - Code blocks (monospace formatting)
  - Tables for API lists, permission matrices
  - Callout boxes for coding-agent prompts (Chapter 6)
  - Checklist formatting for setup steps
- Streaming LLM responses (show progress during generation)
- Basic error handling and retry logic for LLM calls

**Success criteria:**
- Output document is 30–80 pages, well-structured, and a developer could use it immediately without editing.

---

## MVP 3 — Next.js Frontend

**Goal:** Replace CLI/Postman with a real web interface.

**What it includes:**
- Next.js project scaffolded (App Router)
- shadcn/ui for components
- Multi-step Q&A form (one question at a time, progress bar)
- Blueprint generation screen (live progress — "Generating Chapter 3 of 10...")
- Download button for `.docx`
- Basic responsive layout (desktop first, mobile later)
- FastAPI CORS configured for Next.js dev server

**What it excludes:**
- User accounts / auth
- Blueprint history
- MongoDB (still flat files)

**Success criteria:**
- A non-technical user can go from landing page → answer questions → download blueprint without needing Postman or CLI.

---

## MVP 4 — Adaptive Intelligence

**Goal:** Make the Q&A flow smart — questions adapt based on previous answers.

**What it includes:**
- Adaptive question branching logic:
  - Stack = Spring Boot → ask about MongoDB Atlas vs local
  - Domain = e-commerce → ask about payment gateway
  - Domain = learning platform → ask about topic tree depth
  - Scale = enterprise → add compliance questions
- Domain detection from initial app description
- Question set expands from 10 to 15–20 based on domain
- MongoDB integration (store sessions, answers, generated blueprints)
- Blueprint retrieval by session ID

**Success criteria:**
- Two different app types (e.g. e-commerce vs learning platform) produce noticeably different question sets and blueprint content.

---

## MVP 5 — Auth, History & Production Deploy

**Goal:** Ship a real, usable product that people can sign up for.

**What it includes:**
- User authentication (email + password, JWT)
- Blueprint history per user (list past blueprints, re-download)
- Cloud deployment (provider TBD)
- CI/CD pipeline (GitHub Actions)
- Custom domain + SSL
- Basic usage analytics (how many blueprints generated, by domain)

**Success criteria:**
- App is live at a public URL. A user can sign up, generate a blueprint, and come back later to re-download it.

---

## MVP 6 — Polish & Growth (Post-Launch)

**What it includes:**
- PDF export option (WeasyPrint)
- Domain-specific module packs (e-commerce, learning platform, health app)
- Monetisation layer (freemium — 1 free blueprint, subscription for unlimited)
- Prompt optimisation for specific stacks (Spring Boot, Next.js, Django, etc.)
- Share blueprint via link (public URL)
- Feedback system (rate your blueprint)

---

## Build Order Summary

| MVP | Focus | Shippable? |
|---|---|---|
| MVP 1 | Core loop — questions → LLM → .docx | Internal only (Postman) |
| MVP 2 | Output quality + formatting | Internal only (Postman) |
| MVP 3 | Next.js frontend | Yes — share with testers |
| MVP 4 | Adaptive Q&A + MongoDB | Yes — real beta |
| MVP 5 | Auth + cloud deploy | Yes — public launch |
| MVP 6 | Polish + monetisation | Yes — growth phase |

---

## Project Folder Structure (Target)

```
vishkar/
├── plan.md                         # This file
├── backend/                        # FastAPI backend
│   ├── app/
│   │   ├── main.py                 # FastAPI app entry point
│   │   ├── routers/                # API route handlers
│   │   ├── services/               # Business logic (LLM calls, doc gen)
│   │   ├── models/                 # Pydantic models
│   │   ├── prompts/                # Chapter prompt templates
│   │   └── config.py               # Settings / env vars
│   ├── requirements.txt
│   └── .env.example
├── frontend/                       # Next.js app (MVP 3+)
│   └── (scaffolded at MVP 3)
└── docs/                           # Planning docs
    └── vishkar-context.md
```

---

*Plan created: 2026-04-09*
*Current phase: MVP 1*
