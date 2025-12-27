# CLI Documentation

The CLI is the core interface of **AI Term**. It interacts with the users via text or voice, manages the chat history, and orchestrates calls to LLM, STT, and TTS services.

## Overview

The CLI is built using [Textual](https://textual.textualize.io/), a TUI framework for Python.

### Entry Point

The application entry point is `src/cli/main.py`, which initializes the `ChatApp` class.

```python
# src/cli/main.py
def main():
    """Entry point for the CLI app."""
    app = ChatApp()
    app.run()
```

## structure

- **`src/cli/ui`**: Contains all UI components (Screens, Widgets, Styles).
- **`src/cli/core`**: Contains business logic (Agent, Audio Client, MCP Manager).
- **`src/cli/db`**: Database models and engine using `SQLAlchemy` and `aiosqlite`.
- **`src/cli/config.py`**: Configuration management.

## API Reference

::: src.cli.main
