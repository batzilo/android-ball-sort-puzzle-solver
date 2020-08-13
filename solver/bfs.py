"""A modified BFS algorithm for the Android Bubble Sort Puzzle Solver."""

from collections import deque

from solver.trie import Trie
from solver.state import is_solved_state
from solver.state import count_finished_tubes
from solver.state import get_next_states


class QuantizedDoubleEndedPriorityQueue:
    """A Quantized version of the deque data structure."""

    def __init__(self):
        """Create a QuantizedDoubleEndedPriorityQueue."""
        self.d = {}
        self.count = 0

    def add(self, rank, state, moves):
        """Add a state to QuantizedDoubleEndedPriorityQueue."""
        if rank not in self.d:
            self.d[rank] = deque()
        self.d[rank].append((state, moves))
        self.count += 1

    def get(self):
        """Return the next state to be checked."""
        rank = max(self.d.keys())

        ret = self.d[rank].popleft()

        if len(self.d[rank]) == 0:
            del self.d[rank]

        self.count -= 1
        return ret


def bfs(initial_state):
    """Run the modified BFS algorithm."""
    states = QuantizedDoubleEndedPriorityQueue()

    rank = count_finished_tubes(initial_state)
    states.add(rank, initial_state, [])

    visited_states = Trie()

    while states.count > 0:
        # print("#" * (len(states) // 100))
        # print("#" * (len(visited_state_strings) // 10))

        state, moves = states.get()

        # print("")
        # print("")
        # print(f"BFS state is: {state}")

        if visited_states.contains(state):
            continue

        if is_solved_state(state):
            return moves

        visited_states.add(state)

        for next_state, next_moves in get_next_states(state, moves):
            if visited_states.contains(next_state):
                continue

            rank = count_finished_tubes(next_state)
            states.add(rank, next_state, next_moves)
