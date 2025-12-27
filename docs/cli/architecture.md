# Architecture

## High-Level Design

```mermaid
graph TD
    User[User] <--> TUI[Textual CLI App]
    TUI <--> Agent[Chat Agent]
    TUI <--> Audio[Audio Client]
    
    Agent <--> LLM[LLM Provider]
    Audio <--> STT[STT Service]
    Audio <--> TTS[TTS Service]
    
    TUI <--> DB[(SQLite DB)]
```

## Core Components

### Chat Agent
The `ChatAgent` (`src.cli.core.agent`) handles interaction with the LLM using LangChain. It manages system prompts (including speech optimization) and tool calling.

::: src.cli.core.agent.ChatAgent

### Audio Client
The `AudioClient` (`src.cli.core.audio_client`) communicates with the STT and TTS microservices.

::: src.cli.core.audio_client.AudioClient

### MCP Manager
The `MCPManager` (`src.cli.core.mcp_manager`) orchestrates Model Context Protocol servers, allowing the agent to use external tools.

::: src.cli.core.mcp_manager.MCPManager
