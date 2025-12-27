# CLI Documentation

The CLI is the core interface of **AI Term**. It interacts with the users via text or voice, manages the chat history, and orchestrates calls to LLM, STT, and TTS services.

## Overview

The CLI is built using [Textual](https://textual.textualize.io/), a TUI framework for Python.

### Entry Point

The application entry point is `src/ai_term/cli/main.py`, which initializes the `ChatApp` class.

```python
# src/ai_term/cli/main.py
def main():
    """Entry point for the CLI app."""
    app = ChatApp()
    app.run()
```

## Structure

- **`src/ai_term/cli/ui`**: Contains all UI components (Screens, Widgets, Styles).
- **`src/ai_term/cli/core`**: Contains business logic (Agent, Audio Client, MCP Manager).
- **`src/ai_term/cli/db`**: Database models and engine using `SQLAlchemy` and `aiosqlite`.
- **`src/ai_term/cli/config.py`**: Configuration management.

## API Reference

::: ai_term.cli.main
