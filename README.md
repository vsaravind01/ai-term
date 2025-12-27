# AI-Term

**AI-Term** is a voice-enabled terminal assistant that integrates LLMs (Large Language Models), Speech-to-Text (STT), and Text-to-Speech (TTS) into a powerful Command Line Interface (CLI) experience.

![AI Term Banner](docs/img/banner.png)

## Features

- **🗣️ Voice Interaction**: Talk to your terminal and hear responses back.
- **🧠 LLM Integration**: Support for Local (Ollama) and Cloud (OpenAI, Anthropic) models.
- **🔌 MCP Support**: Model Context Protocol client for extensible tool use.
- **🖥️ TUI Interface**: Beautiful, responsive terminal UI built with [Textual](https://textual.textualize.io/).
- **⚙️ Dynamic Configuration**: Easy-to-use settings screen for managing providers and secrets.

## Prerequisites

- Python 3.10+
- `uv` (recommended) or `pip`
- `ffmpeg` (required for audio processing)

## Installation

1. **Clone the repository:**
   ```bash
   git clone https://github.com/vsaravind01/ai-term.git
   cd ai-term
   ```

2. **Install dependencies:**
   ```bash
   uv sync
   # OR with pip
   pip install -e .
   ```

## Quick Start

The application runs as a distributed system with a main CLI and two support microservices.

### 1. Start Support Services
Open two separate terminal windows/tabs:

**STT Service (Port 8001):**
```bash
uv run uvicorn ai_term.stt.main:app --port 8001
```

**TTS Service (Port 8002):**
```bash
uv run uvicorn ai_term.tts.main:app --port 8002
```

### 2. Start the CLI
In your main terminal:

```bash
uv run ai-term
```

## Documentation

Full documentation is available in the `docs/` directory. To view it locally:

```bash
uv run mkdocs serve
```

- [**Setup Guide**](docs/setup.md)
- [**CLI Documentation**](docs/cli/index.md)
- [**API Reference**](docs/api.md)

## License

[MIT](LICENSE)