"""This is a module-level docstring.
It should appear purple and italic if your settings are working.
"""


def greet(name: str) -> str:
    """Return a friendly greeting for the given name."""
    return f"Hello, {name}!"


class Greeter:
    """A simple greeter class."""

    def __init__(self, name: str):
        """Initialize with a name."""
        self.name = name
