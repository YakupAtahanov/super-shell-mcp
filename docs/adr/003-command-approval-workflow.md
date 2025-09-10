# ADR 003: Command Approval Workflow

## Status

Accepted

## Context

When executing shell commands, there's a middle ground between completely safe commands and forbidden commands. Some commands can modify the system in potentially harmful ways but are still necessary for legitimate use cases. We need a mechanism to handle these commands safely.

Options considered:
1. Reject all potentially dangerous commands
2. Allow all commands with appropriate warnings
3. Implement an approval workflow for commands that require additional verification

## Decision

We will implement an approval workflow for commands that are potentially dangerous but still necessary. This workflow will:

1. Queue commands marked as requiring approval
2. Provide tools to list pending commands
3. Allow explicit approval or denial of pending commands
4. Execute approved commands and reject denied commands

This approach balances security with usability by allowing potentially dangerous commands to be executed after explicit approval.

## Consequences

### Positive

- Provides a middle ground between allowing and forbidding commands
- Creates an audit trail of command approvals
- Allows for human judgment in borderline cases
- Enables safe use of necessary system-modifying commands
- Prevents accidental execution of dangerous commands

### Negative

- Introduces asynchronous workflow for command execution
- Requires additional user interaction for approval
- May create confusion if approvals are delayed or forgotten

## Implementation (Python)

The approval workflow uses a queue of pending commands represented by a dataclass:

```python
from dataclasses import dataclass
from typing import Callable, List, Optional

@dataclass
class PendingCommand:
    id: str
    command: str
    args: List[str]
    requested_at: float
    requested_by: Optional[str]
    resolve: Callable[[CommandResult], None]
    reject: Callable[[Exception], None]
```

When a command requiring approval is executed, it is added to the queue and an event is emitted:

```python
async def _queue_command_for_approval(self, command: str, args: Optional[List[str]], requested_by: Optional[str]) -> CommandResult:
    loop = asyncio.get_event_loop()
    fut = loop.create_future()
    cmd_id = str(uuid.uuid4())
    pending = PendingCommand(
        id=cmd_id,
        command=command,
        args=list(args or []),
        requested_at=loop.time(),
        requested_by=requested_by,
        resolve=lambda res: (not fut.done()) and fut.set_result(res),
        reject=lambda err: (not fut.done()) and fut.set_exception(err),
    )
    self.pending_commands[cmd_id] = pending
    self.emit("command:pending", pending)
    loop.call_later(5.0, self._emit_timeout_if_pending, cmd_id)
    return await fut
```

The MCP server exposes tools to list, approve, and deny pending commands:

```python
@mcp.tool(name="get_pending_commands", description="Get pending commands")
async def get_pending_commands() -> str:
    ...

@mcp.tool(name="approve_command", args={"commandId": {"type": "string", "required": True}})
async def approve_command(commandId: str) -> str:
    ...

@mcp.tool(name="deny_command", args={"commandId": {"type": "string", "required": True}, "reason": {"type": "string"}})
async def deny_command(commandId: str, reason: Optional[str] = None) -> str:
    ...
```

This workflow ensures that potentially dangerous commands are only executed after explicit approval, providing an additional layer of security.