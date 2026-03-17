# URL Shortener Backend

FastAPI backend skeleton for a URL shortener app.

## Suggested `uv` setup

```bash
uv sync
uv run uvicorn app.main:app --reload
```

## Structure

```text
backend/
├── app/
│   ├── api/
│   │   └── routes/
│   ├── core/
│   ├── db/
│   ├── models/
│   ├── schemas/
│   └── services/
└── pyproject.toml
```

