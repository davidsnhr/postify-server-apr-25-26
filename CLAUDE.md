# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project

**Postify** — FastAPI backend API. Early-stage project; structure will grow over time.

## Environment

Uses a Python virtual environment at `.venv`. Activate before running anything:

```bash
source .venv/bin/activate
```

## Running the server

```bash
uvicorn main:app --reload
```

## Key dependencies

- **FastAPI 0.136** — async web framework
- **Uvicorn** — ASGI server
- **Pydantic v2** — data validation and schemas
- **python-dotenv** — loads `.env` files (gitignored)
- **Sentry SDK** — error tracking

## Architecture

Single entry point: `main.py` instantiates the FastAPI `app`. As the project grows, expect routes, services, and Pydantic schemas to be organized into separate modules.

No database or ORM is configured yet. No test runner is configured yet.

## Companion project

Frontend lives at `../ui-postify`.
