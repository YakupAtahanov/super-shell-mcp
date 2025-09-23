[![MseeP.ai Security Assessment Badge](https://mseep.net/pr/cfdude-super-shell-mcp-badge.png)](https://mseep.ai/app/cfdude-super-shell-mcp)

# Super Shell MCP Server (Python)

[![smithery badge](https://smithery.ai/badge/@cfdude/super-shell-mcp)](https://smithery.ai/package/@cfdude/super-shell-mcp)

A Python MCP (Model Context Protocol) server for executing shell commands on Linux with secure **whitelisting** and **approval workflows**.

## ✨ Features

- Linux shell command execution via MCP
- Automatic Linux shell detection and selection
- Security levels:
  - **Safe** → runs immediately
  - **Requires Approval** → held until explicitly approved
  - **Forbidden** → never executed
- Linux-specific command whitelists included
- File-based logging (`logs/super-shell-mcp.log`)
- Tools for command management and platform diagnostics

## 🚀 Installation

```bash
# Clone the repository
git clone https://github.com/cfdude/super-shell-mcp.git
cd super-shell-mcp

# Create a virtual environment
python -m venv .venv
source .venv/bin/activate

# Install dependencies
pip install -r requirements.txt
```

Or with [uv](https://github.com/astral-sh/uv):

```bash
uv run src/main.py
```

## ▶️ Usage

Start the server (stdio transport):

```bash
python src/main.py
```

Logs will be written to `logs/super-shell-mcp.log`.

### Claude Desktop Configuration

Edit `claude_desktop_config.json`:

```json
"super-shell-mcp": {
  "command": "python",
  "args": ["src/main.py"],
  "cwd": "/absolute/path/to/super-shell-mcp",
  "env": { "PYTHONUNBUFFERED": "1" },
  "alwaysAllow": false,
  "disabled": false
}
```

With **uv**:

```json
"super-shell-mcp": {
  "command": "uv",
  "args": ["run", "src/main.py"],
  "cwd": "/absolute/path/to/super-shell-mcp",
  "env": { "PYTHONUNBUFFERED": "1" },
  "alwaysAllow": false,
  "disabled": false
}
```

## 🛠️ Available Tools

- `get_platform_info` → OS + shell info
- `execute_command` → run a shell command
- `get_whitelist` → list whitelisted commands
- `add_to_whitelist` → add a command with security level
- `update_security_level` → change command security
- `remove_from_whitelist` → remove command
- `get_pending_commands` → list commands awaiting approval
- `approve_command` → approve queued command
- `deny_command` → deny queued command
- `get_running_commands` → list currently executing commands
- `cancel_command` → cancel a running command (like Ctrl+C)

## ✅ Testing

Run tests with:

```bash
pytest -q
```

Run example client:

```bash
python examples/client_example.py
```

## 🐳 Docker

```bash
docker build -t super-shell-mcp:py .
docker run --rm -it super-shell-mcp:py
```

## 📜 License

MIT License. See the LICENSE file for details.
