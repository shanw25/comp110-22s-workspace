"""Demonstrate defining a module imported elsewhere."""


def powerful(x: float, n: float) -> float:
    """Raise x to the power of n."""
    return x ** n


print(__name__)


def maina() -> None:
    print("a")


if __name__ == "__main__":
    maina()