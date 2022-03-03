"""love function 2022/02/03."""


def love(name: str) -> str:
    """Given a name as a parameter, returns a loving string."""
    return f"I love you {name}"


def spread_love(to: str, n: int) -> str:
    """Generates a string that repeats a loving message n times."""
    love_notes: str = ""
    count: int = 0
    while count < n:
        love_notes += love(to) + "\n"
        count += 1
    return love_notes