"""State helper functions for the Android Bubble Sort Puzzle Solver."""


def _get_number_of_tubes(state):
    """Get the number of tubes."""
    return len(state.split(" "))


def _get_start_of_tube(i):
    """Get the start position of tube i."""
    return i * 5


# def normalize(state):
#     """Normalize state, so that two "equal" states become the same."""
#     tubes = state.split(" ")
#     sort(tubes)
#     ...


def count_finished_tubes(state):
    """Count how many tubes are finished."""
    n_finished_tubes = 0

    n_tubes = _get_number_of_tubes(state)

    for t in range(n_tubes):
        is_tube_finished = True

        tube_start = _get_start_of_tube(t)
        c = state[tube_start]

        # Should we consider all-empty-tubes finished?
        # if c == "_":
        #     continue

        for k in range(4):
            if c != state[tube_start + k]:
                is_tube_finished = False

        if is_tube_finished:
            n_finished_tubes += 1

    return n_finished_tubes


def is_solved_state(state):
    """Check if the given state is solved."""
    return _get_number_of_tubes(state) == count_finished_tubes(state)


def get_next_states(current_state, current_moves):
    """Generate the next possible states from the given current state."""
    n_tubes = _get_number_of_tubes(current_state)
    # print(f"n_tubes is {n_tubes}")

    # The list ret will hold the next possible states
    ret = []

    for i in range(n_tubes):
        # print(" ")
        # print(f"Examining src tube {i+1}")

        start_src_tube = _get_start_of_tube(i)

        # print(f"Tube {i+1} starts in position {start_src_tube}"
        #       f" with : {current_state[start_src_tube]}")

        number_of_src_empty_slots = 0
        possible_next_src_empty_slot_pos = (
            start_src_tube + number_of_src_empty_slots
        )
        while (
            possible_next_src_empty_slot_pos < len(current_state)
            and current_state[possible_next_src_empty_slot_pos] == "_"
        ):
            number_of_src_empty_slots += 1
            possible_next_src_empty_slot_pos = (
                start_src_tube + number_of_src_empty_slots
            )

        first_ball_in_tube = 0
        possible_next_ball_pos = start_src_tube + first_ball_in_tube
        while (
            possible_next_ball_pos < len(current_state)
            and current_state[possible_next_ball_pos] == "_"
        ):
            # print("Skipping an empty position")
            first_ball_in_tube += 1
            possible_next_ball_pos = start_src_tube + first_ball_in_tube

        if first_ball_in_tube == 4:
            # This is an empty tube
            # print("Cannot move balls from empty tube")
            continue

        # print(f"Ball(s) start at position"
        #       f" {start_src_tube + first_ball_in_tube}")

        src_ball_color = current_state[start_src_tube + first_ball_in_tube]

        number_of_same_balls = 1
        possible_next_ball_pos = (
            start_src_tube + first_ball_in_tube + number_of_same_balls
        )
        while (
            possible_next_ball_pos < len(current_state)
            and current_state[possible_next_ball_pos] == src_ball_color
        ):
            number_of_same_balls += 1
            possible_next_ball_pos = (
                start_src_tube + first_ball_in_tube + number_of_same_balls
            )

        # print(f"Found {number_of_same_balls} ball(s) of same color")

        if number_of_same_balls == 4:
            # print("Refused to move from finished tube")
            continue

        # print(f"I want to move {number_of_same_balls} ball(s)"
        #       f" of color {src_ball_color}")

        for j in range(n_tubes):

            if i == j:
                continue

            # print(f"Examining dst tube {j+1}")

            start_dst_tube = _get_start_of_tube(j)

            if current_state[start_dst_tube] != "_":
                # print(f"Dst tube {j+1} is full")
                continue

            number_of_empty_slots = 1
            possible_next_empty_slot_pos = (
                start_dst_tube + number_of_empty_slots
            )
            while (
                possible_next_empty_slot_pos < len(current_state)
                and current_state[possible_next_empty_slot_pos] == "_"
            ):
                number_of_empty_slots += 1
                possible_next_empty_slot_pos = (
                    start_dst_tube + number_of_empty_slots
                )

            # print(f"Found {number_of_empty_slots} empty slots")

            if number_of_same_balls > number_of_empty_slots:
                # print(f"Cannot move {number_of_same_balls} ball(s)"
                #       f" to {number_of_empty_slots} empty slot(s)")
                continue

            if (
                number_of_empty_slots == 4
                and number_of_src_empty_slots + number_of_same_balls == 4
            ):
                continue

            if (
                number_of_empty_slots == 4
                or current_state[start_dst_tube + number_of_empty_slots]
                == src_ball_color
            ):  # noqa
                # print(f"Can move {number_of_same_balls} balls"
                #       f" from src tube {i+1}"
                #       f" to dst tube {j+1}")
                pass
            else:
                continue

            # print(f"The current state is {current_state}")

            # Generate the possible state
            next_state = list(current_state[:])
            for k in range(number_of_same_balls):
                next_state[start_src_tube + first_ball_in_tube + k] = "_"
                next_state[
                    start_dst_tube + number_of_empty_slots - k - 1
                ] = src_ball_color  # noqa

            next_state = "".join(next_state).strip()

            # print(f"The    next state is {next_state}")
            ret.append(
                (next_state, current_moves + ["%d --> %d" % (i + 1, j + 1)])
            )

    return ret
