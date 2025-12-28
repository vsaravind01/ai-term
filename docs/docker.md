# Docker Guide

ai_term supports Docker for ease of deployment. This guide covers how to use Docker to run the STT (Speech-to-Text) and TTS (Text-to-Speech) services.

## Overview

The `docker-compose.yml` file in the root directory defines two services:
- **`stt`**: Whisper-based transcription service.
- **`tts`**: Coqui-based speech synthesis service.

## Quick Start

```bash
docker compose up -d --build
```

This will:
1. Build the images for both services.
2. Map the services to the following ports:
    - STT: `http://localhost:8901`
    - TTS: `http://localhost:8902`
3. Mount local volumes for model caching to avoid re-downloading large models on every restart.

## Port Configuration

By default, we use unique ports to avoid conflicts with other local services:

| Service | Container Port | Host Port |
|---------|----------------|-----------|
| STT     | 8001           | 8901      |
| TTS     | 8002           | 8902      |

You can customize these in `docker-compose.yml`.

## Volumes and Caching

To speed up startup, the services mount local cache directories:
- **Whisper Models**: `~/.cache/whisper` -> `/root/.cache/whisper`
- **TTS Models**: `~/.local/share/tts` -> `/root/.local/share/tts`

## GPU Support

If you have an NVIDIA GPU, you can enable hardware acceleration by modifying the `Dockerfile` and `docker-compose.yml` to use CUDA-enabled base images (e.g., `pytorch/pytorch`).

> [!NOTE]
> The default setup uses CPU for maximum compatibility. Performance will depend on your CPU's speed.
