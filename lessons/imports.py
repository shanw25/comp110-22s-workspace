"""Examples of importing Python."""

from lessons import helpers
from lessons.helpers import maina


def main() -> None:
    """Entrypoint of program."""
    print(helpers.powerful(2, 4))
    maina()


if __name__ == "__main__":
    main()