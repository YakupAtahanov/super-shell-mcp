# ADR 002: Using MCP for Shell Command Execution

## Status

Accepted

## Context

There are several ways to provide shell command execution capabilities to AI assistants:

1. Custom API endpoints
2. Direct integration with specific AI platforms
3. Standardized protocols like MCP (Model Context Protocol)

Each approach has different tradeoffs in terms of flexibility, security, and integration complexity. We need to decide on the most appropriate approach for our shell command execution service.

## Decision

We will implement shell command execution as an MCP server for the following reasons:

1. **Standardization**: MCP is an emerging standard for AI tool integration, supported by major AI platforms like Anthropic's Claude.
2. **Discoverability**: MCP provides built-in tool discovery, allowing AI assistants to automatically learn about available commands and their parameters.
3. **Security**: MCP's structured approach allows for clear security boundaries and validation of inputs.
4. **Flexibility**: MCP servers can be used with any MCP-compatible client, not just specific AI platforms.
5. **Future-proofing**: As more AI platforms adopt MCP, our implementation will be compatible without changes.

## Consequences

### Positive

- Works with any MCP-compatible client (Claude Desktop, etc.)
- Provides structured tool definitions with clear parameter schemas
- Enables dynamic tool discovery
- Follows an emerging industry standard
- Separates concerns between command execution and AI integration

### Negative

- MCP is still an evolving standard
- Requires understanding of MCP concepts and implementation details
- May have more overhead than a direct, custom integration

## Implementation (Python)

We implement the MCP server using the Python MCP SDK (FastMCP):

```python
from typing import List, Optional
from mcp.server.fastmcp import FastMCP

mcp = FastMCP(name="super-shell-mcp", version="2.0.13")

@mcp.tool(
    name="execute_command",
    description="Execute a shell command on the current platform",
    args={
        "command": {"type": "string", "required": True},
        "args": {"type": "array", "items": {"type": "string"}, "required": False},
    },
)
async def execute_command(command: str, args: Optional[List[str]] = None) -> str:
    ...  # delegate to CommandService

async def _run_stdio() -> None:
    await mcp.run_stdio()
```

The server uses stdio transport for compatibility with MCP clients (Claude Desktop, Roo Code, etc.) via `mcp.run_stdio()`.