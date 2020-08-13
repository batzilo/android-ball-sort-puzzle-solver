"""The main module of the Android Bubble Sort Puzzle Solver."""

import sys

from solver.colors import get_color_key_from_value
from solver.bfs import bfs


def _ordinal(k):
    if k == 1:
        return " 1st"
    if k == 2:
        return " 2nd"
    if k == 3:
        return " 3rd"
    return "%2dth" % k


def _ask_for_ball_color_key(n_tube, n_spot):
    print(
        f"Give the color (or Empty)"
        f" of the {_ordinal(n_spot)} top-most ball"
        f" in the {_ordinal(n_tube)} tube"
    )
    content = input()
    if content == "Empty":
        return "_"
    return get_color_key_from_value(content)


def ask_for_original_state():
    """Ask the user about the original placement of balls into tubes."""
    print("How many tubes are there?")
    num_of_tubes = int(input())

    original_state = []
    for i in range(num_of_tubes):
        for j in range(4):
            content = _ask_for_ball_color_key(i + 1, j + 1)
            original_state.append(content)
        original_state.append(" ")

    # Drop the last space
    del original_state[-1]

    return "".join(original_state)


def main():
    """Solve the Android Bubble Sort Puzzle."""
    original_state = ask_for_original_state()
    # print(original_state)

    print("")
    print("")
    print("Thinking ...")
    print("")
    print("")

    moves = bfs(original_state)

    print("BOOM!")
    print("\n".join(moves))
    return 0


if __name__ == "__main__":
    sys.exit(main())
