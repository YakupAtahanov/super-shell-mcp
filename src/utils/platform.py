from __future__ import annotations

import os
from pathlib import Path
from typing import List


def get_default_shell() -> str:
    """
    Get the default shell for Linux.
    """
    return os.environ.get("SHELL", "/bin/bash")


def validate_shell_path(shell_path: str) -> bool:
    """
    Validate if a shell path exists and is executable.
    """
    try:
        p = Path(shell_path)
        return p.exists() and p.is_file()
    except Exception:
        return False


def get_shell_suggestions() -> List[str]:
    """
    Get shell suggestions for Linux.
    """
    return ["/bin/bash", "/bin/sh", "/usr/bin/bash", "/usr/bin/zsh"]


def get_common_shell_locations() -> List[str]:
    """
    Get common locations for shells on Linux.
    """
    return ["/bin/bash", "/bin/sh", "/usr/bin/bash", "/usr/bin/zsh"]


def get_shell_configuration_help() -> str:
    """
    Get helpful message for shell configuration on Linux.
    """
    suggestions = get_shell_suggestions()
    locations = get_common_shell_locations()

    message = "Shell Configuration Help:\n\n"
    message += "Platform: Linux\n\n"
    message += "Suggested shells for Linux:\n"
    for shell in suggestions:
        message += f"- {shell}\n"

    message += "\nCommon shell locations on Linux:\n"
    for location in locations:
        message += f"- {location}\n"

    message += "\nTo configure a custom shell, provide the full path to the shell executable."
    return message
