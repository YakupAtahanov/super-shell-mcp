# ADR 004: Linux-Only Shell Support

## Status

Accepted

## Context

The original Mac Shell MCP server was designed specifically for macOS with ZSH shell. After initial cross-platform support, we've decided to focus specifically on Linux to simplify the codebase and reduce complexity.

Key benefits of Linux-only approach:

1. **Simplified Codebase**: No need for platform detection or conditional logic
2. **Consistent Environment**: All users run on the same platform with predictable behavior
3. **Linux-First Commands**: Can focus on Linux-specific commands and tools
4. **Reduced Testing Surface**: Only need to test on Linux environments

## Decision

We will refactor the server to be Linux-only with the following changes:

1. **Remove Platform Detection**: Eliminate all platform detection logic
2. **Linux Shell Selection**: Use Linux-specific shell defaults (bash, sh, zsh)
3. **Linux Path Handling**: Use standard Unix path handling
4. **Linux Command Whitelists**: Implement Linux-specific command whitelists only
5. **Simplified Documentation**: Update all documentation to reflect Linux-only support

## Consequences

### Positive

- Simplified codebase with no platform detection logic
- Consistent Linux environment for all users
- Focused command whitelist optimized for Linux
- Reduced testing complexity (Linux only)
- Better performance without platform detection overhead

### Negative

- Limited to Linux users only
- Cannot be used on Windows or macOS
- Reduced potential user base

## Implementation

The implementation is simplified for Linux-only:

```python
def get_default_shell() -> str:
    """
    Get the default shell for Linux.
    """
    return os.environ.get("SHELL", "/bin/bash")
```

Linux-specific shell suggestions:

```python
def get_shell_suggestions() -> List[str]:
    """
    Get shell suggestions for Linux.
    """
    return ["/bin/bash", "/bin/sh", "/usr/bin/bash", "/usr/bin/zsh"]
```

Linux command whitelists:

```python
def get_platform_specific_commands() -> List[CommandWhitelistEntry]:
    """
    Get all Linux-specific commands (safe, approval, and forbidden).
    """
    # Add common safe commands
    common_safe_commands = get_common_safe_commands()
    
    # Add Linux-specific commands
    safe_commands = get_linux_safe_commands()
    approval_commands = get_linux_approval_commands()
    forbidden_commands = get_linux_forbidden_commands()

    # Combine all commands
    return [*common_safe_commands, *safe_commands, *approval_commands, *forbidden_commands]
```

Standard Unix path handling:

```python
# Extract the base command using os.path.basename for Unix compatibility
base_command = os.path.basename(command)
```