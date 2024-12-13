
import numpy as np


direction_dict: dict[str, dict[str, list[str]]] = {
    "\\": {"N": ["W"], "E": ["S"], "S": ["E"], "W": ["N"]},
    r"/": {"N": ["E"], "E": ["N"], "S": ["W"], "W": ["S"]},
    r"|": {"N": ["N"], "E": ["N", "S"], "W": ["N", "S"], "S": ["S"]},
    r"-": {"N": ["W", "E"], "E": ["E"], "W": ["W"], "S": ["W", "E"]},
    r".": {"N": ["N"], "E": ["E"], "S": ["S"], "W": ["W"]},
}

direction_move: dict[str, tuple[int, int]] = {
    "N": (-1, 0),
    "E": (0, 1),
    "S": (1, 0),
    "W": (0, -1),
}


def t_add(a: tuple[int, ...], b: tuple[int, ...]) -> tuple[int, ...]:
    return tuple(map(sum, zip(a, b)))


def puzzle(puzzle_input: list[str]) -> int:
    puzzle_matrix = np.array([list(x) for x in puzzle_input], ndmin=2)

    stored: list[tuple[int, int, str]] = [(0, 0, "E")]
    visited: set[tuple[int, int, str]] = set()

    grid_size = puzzle_matrix.shape
    for x, y, direction in stored:
        # border check
        if x >= grid_size[0] or x < 0:
            continue
        if y >= grid_size[1] or y < 0:
            continue

        self_val = puzzle_matrix[x][y]
        if (x, y, direction) in visited and self_val != ".":
            continue
        
        new_dirs = direction_dict[self_val][direction]
        visited.add((x, y, direction))

        for i in new_dirs:
            new_plus = direction_move[i]
            n_x, n_y = t_add(new_plus, (x, y))
            stored.append((n_x, n_y, i))

    coord_set = set((x, y) for x, y, _ in visited)

    return len(coord_set)


if __name__ == "__main__":
    import sys
    import os
    from io import TextIOWrapper
    from typing import TextIO

    try:
        final: bool = "final" in sys.argv
        file: bool = "file" in sys.argv
        clock: bool = "time" in sys.argv

    except IndexError:
        final = False
        file = False
        clock = False

    dir_path: str = os.path.dirname(os.path.realpath(__file__))

    if file:
        orig_stdout: TextIO = sys.stdout
        f: TextIOWrapper = open("out.txt", "w")
        sys.stdout = f

    if clock:
        import time

        start: float = time.time()

    if final:
        puzzle_input: list[str] = open(f"{dir_path}/input.txt", "r").readlines()
        # puzzle_input_r: list[str] = [x.rstrip() for x in puzzle_input]
        puzzle_input_r: list[str] = [str(x.rstrip()) for x in puzzle_input]
        print(puzzle(puzzle_input_r))

    else:
        puzzle_input: list[str] = open(f"{dir_path}/test.txt", "r").readlines()
        # puzzle_input_r: list[str] = [x.rstrip() for x in puzzle_input]
        puzzle_input_r: list[str] = [str(x.rstrip()) for x in puzzle_input]
        assert puzzle(puzzle_input_r) == 46

    if clock:
        print("time: ", time.time() - start)  # type: ignore

    if file:
        sys.stdout = orig_stdout  # type: ignore
        f.close()  # type: ignore