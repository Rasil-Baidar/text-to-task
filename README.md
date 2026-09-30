# text-to-task

A FastAPI service that turns natural-language text into tasks using a locally-running Ollama model (`llama3.1`).

## Prerequisites

- **Python 3.14+**
- **[uv](https://docs.astral.sh/uv/getting-started/installation/)** — Python package/venv manager
  ```bash
  curl -LsSf https://astral.sh/uv/install.sh | sh
  ```
- **[Ollama](https://ollama.com/download)** — running locally on the default port (`11434`)
  ```bash
  # macOS
  brew install ollama
  ```

## Setup

1. **Clone & enter the repo**
   ```bash
   git clone <repo-url>
   cd text-to-task
   ```

2. **Install dependencies** (creates `.venv` and installs from `uv.lock`)
   ```bash
   make install
   # or: uv sync
   ```

3. **Start Ollama and pull the model** (one-time)
   ```bash
   ollama serve            # in a separate terminal, if not already running
   ollama pull llama3.1
   ```

## Run

- **Dev mode** (auto-reload on file changes):
  ```bash
  make dev
  ```
- **Production-style run**:
  ```bash
  make run
  ```

The API listens on `http://localhost:8000`. Interactive docs are available at `http://localhost:8000/docs`.

## Try it

```bash
curl -X POST http://localhost:8000/api/v1/check-mcp \
  -H "Content-Type: application/json" \
  -d '{"text": "Remind me to buy milk tomorrow at 9am"}'
```

## Project layout

```
src/text_to_task/
├── app.py              # FastAPI app entrypoint
└── api/
    ├── main.py         # Router registration (prefix: /api/v1)
    ├── routes/         # HTTP route definitions
    └── handler/        # Business logic (Ollama calls, etc.)
```
