"""Example of helper functions for a notebook."""


def add_two_ints(x: int, y: int) -> int:
    """Add x to y."""
    return x + y



dd: dict[str, int] = {"a": 1, "b": 2}
print(dd)
dd.pop(1)
print(dd)