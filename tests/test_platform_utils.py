from src.utils.platform import (
    get_default_shell,
    get_shell_suggestions,
    get_common_shell_locations,
)


def test_get_default_shell_returns_string():
    sh = get_default_shell()
    assert isinstance(sh, str)
    assert len(sh) >= 1


def test_shell_suggestions_returns_linux_shells():
    s = get_shell_suggestions()
    assert isinstance(s, list)
    assert "/bin/bash" in s
    assert "/bin/sh" in s
    assert all(isinstance(x, str) for x in s)


def test_common_shell_locations_returns_list():
    locs = get_common_shell_locations()
    assert isinstance(locs, list)
    assert all(isinstance(x, str) for x in locs)
    assert "/bin/bash" in locs
    assert "/bin/sh" in locs
