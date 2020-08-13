"""Colors used in Android Bubble Sort Puzzle."""

# Assume that 16 colors are enough

EMPTY = "Empty"

COLOR_MAP = {
    "0": "Blue",
    "1": "Brown",
    "2": "Gray",
    "3": "Green",
    "4": "Lblue",
    "5": "Lgreen",
    "6": "Lime",
    "7": "Orange",
    "8": "Pink",
    "9": "Purple",
    "a": "Red",
    "b": "Yellow",
    "c": None,
    "d": None,
    "e": None,
    "f": None,
}


class ColorError(Exception):
    """The color error class."""


def get_color_key_from_value(color_name):
    """Translate color name to color key."""
    for k, v in COLOR_MAP.items():
        if v == color_name:
            return k
    msg = "No such color: %s" % color_name
    raise ColorError(msg)
