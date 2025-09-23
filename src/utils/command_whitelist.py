from __future__ import annotations

from typing import List
from src.services.command_service import (
    CommandSecurityLevel,
    CommandWhitelistEntry,
)

# ---------------------------------------------------------------------------
# Common safe commands
# ---------------------------------------------------------------------------

def get_common_safe_commands() -> List[CommandWhitelistEntry]:
    return [
        CommandWhitelistEntry(
            command="echo",
            security_level=CommandSecurityLevel.SAFE,
            description="Print text to standard output",
        )
    ]


# ---------------------------------------------------------------------------
# Linux safe commands
# ---------------------------------------------------------------------------

def get_linux_safe_commands() -> List[CommandWhitelistEntry]:
    return [
        CommandWhitelistEntry("ls", CommandSecurityLevel.SAFE, "List directory contents"),
        CommandWhitelistEntry("pwd", CommandSecurityLevel.SAFE, "Print working directory"),
        CommandWhitelistEntry("cat", CommandSecurityLevel.SAFE, "Concatenate and print files"),
        CommandWhitelistEntry("grep", CommandSecurityLevel.SAFE, "Search for patterns in files"),
        CommandWhitelistEntry("find", CommandSecurityLevel.SAFE, "Find files in a directory hierarchy"),
        CommandWhitelistEntry("cd", CommandSecurityLevel.SAFE, "Change directory"),
        CommandWhitelistEntry("head", CommandSecurityLevel.SAFE, "Output the first part of files"),
        CommandWhitelistEntry("tail", CommandSecurityLevel.SAFE, "Output the last part of files"),
        CommandWhitelistEntry("wc", CommandSecurityLevel.SAFE, "Print newline, word, and byte counts"),
        CommandWhitelistEntry("whoami", CommandSecurityLevel.SAFE, "Display current user"),
        CommandWhitelistEntry("hostname", CommandSecurityLevel.SAFE, "Display computer name"),
        CommandWhitelistEntry("uname", CommandSecurityLevel.SAFE, "Display system information"),
        CommandWhitelistEntry("which", CommandSecurityLevel.SAFE, "Locate programs"),
        CommandWhitelistEntry("whereis", CommandSecurityLevel.SAFE, "Locate programs"),
    ]


# ---------------------------------------------------------------------------
# Linux commands requiring approval
# ---------------------------------------------------------------------------

def get_linux_approval_commands() -> List[CommandWhitelistEntry]:
    return [
        CommandWhitelistEntry("mv", CommandSecurityLevel.REQUIRES_APPROVAL, "Move (rename) files"),
        CommandWhitelistEntry("cp", CommandSecurityLevel.REQUIRES_APPROVAL, "Copy files and directories"),
        CommandWhitelistEntry("mkdir", CommandSecurityLevel.REQUIRES_APPROVAL, "Create directories"),
        CommandWhitelistEntry("touch", CommandSecurityLevel.REQUIRES_APPROVAL, "Change file timestamps or create empty files"),
        CommandWhitelistEntry("chmod", CommandSecurityLevel.REQUIRES_APPROVAL, "Change file mode bits"),
        CommandWhitelistEntry("chown", CommandSecurityLevel.REQUIRES_APPROVAL, "Change file owner and group"),
        CommandWhitelistEntry("ln", CommandSecurityLevel.REQUIRES_APPROVAL, "Create links"),
        CommandWhitelistEntry("tar", CommandSecurityLevel.REQUIRES_APPROVAL, "Archive files"),
        CommandWhitelistEntry("gzip", CommandSecurityLevel.REQUIRES_APPROVAL, "Compress files"),
        CommandWhitelistEntry("gunzip", CommandSecurityLevel.REQUIRES_APPROVAL, "Decompress files"),
        # Package managers with extended timeouts
        CommandWhitelistEntry("pip", CommandSecurityLevel.REQUIRES_APPROVAL, "Python package manager", timeout_override=600_000),  # 10 minutes
        CommandWhitelistEntry("pip3", CommandSecurityLevel.REQUIRES_APPROVAL, "Python 3 package manager", timeout_override=600_000),  # 10 minutes
        CommandWhitelistEntry("npm", CommandSecurityLevel.REQUIRES_APPROVAL, "Node.js package manager", timeout_override=600_000),  # 10 minutes
        CommandWhitelistEntry("yarn", CommandSecurityLevel.REQUIRES_APPROVAL, "Yarn package manager", timeout_override=600_000),  # 10 minutes
        CommandWhitelistEntry("cargo", CommandSecurityLevel.REQUIRES_APPROVAL, "Rust package manager", timeout_override=600_000),  # 10 minutes
        CommandWhitelistEntry("go", CommandSecurityLevel.REQUIRES_APPROVAL, "Go toolchain", timeout_override=300_000),  # 5 minutes
        CommandWhitelistEntry("apt", CommandSecurityLevel.REQUIRES_APPROVAL, "Debian package manager", timeout_override=600_000),  # 10 minutes
        CommandWhitelistEntry("apt-get", CommandSecurityLevel.REQUIRES_APPROVAL, "Debian package manager", timeout_override=600_000),  # 10 minutes
        CommandWhitelistEntry("yum", CommandSecurityLevel.REQUIRES_APPROVAL, "Red Hat package manager", timeout_override=600_000),  # 10 minutes
        CommandWhitelistEntry("dnf", CommandSecurityLevel.REQUIRES_APPROVAL, "Fedora package manager", timeout_override=600_000),  # 10 minutes
        CommandWhitelistEntry("pacman", CommandSecurityLevel.REQUIRES_APPROVAL, "Arch package manager", timeout_override=600_000),  # 10 minutes
    ]


# ---------------------------------------------------------------------------
# Linux forbidden commands
# ---------------------------------------------------------------------------

def get_linux_forbidden_commands() -> List[CommandWhitelistEntry]:
    return [
        CommandWhitelistEntry("rm", CommandSecurityLevel.FORBIDDEN, "Remove files or directories"),
        CommandWhitelistEntry("sudo", CommandSecurityLevel.FORBIDDEN, "Execute a command as another user"),
        CommandWhitelistEntry("su", CommandSecurityLevel.FORBIDDEN, "Switch user"),
        CommandWhitelistEntry("dd", CommandSecurityLevel.FORBIDDEN, "Convert and copy files"),
        CommandWhitelistEntry("mkfs", CommandSecurityLevel.FORBIDDEN, "Make filesystem"),
        CommandWhitelistEntry("fdisk", CommandSecurityLevel.FORBIDDEN, "Disk partition manipulator"),
        CommandWhitelistEntry("shutdown", CommandSecurityLevel.FORBIDDEN, "Shutdown system"),
        CommandWhitelistEntry("reboot", CommandSecurityLevel.FORBIDDEN, "Reboot system"),
        CommandWhitelistEntry("halt", CommandSecurityLevel.FORBIDDEN, "Halt system"),
        CommandWhitelistEntry("poweroff", CommandSecurityLevel.FORBIDDEN, "Power off system"),
    ]


# ---------------------------------------------------------------------------
# Linux command aggregation
# ---------------------------------------------------------------------------

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
