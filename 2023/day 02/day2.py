from typing import Any

# globals
max_red = 12
max_green = 13
max_blue = 14


def inner_ball_check(ball_split: list[str]) -> bool:
    for ball_grab in ball_split:
        seperate_balls = ball_grab.split(",")
        for i in seperate_balls:
            i_clean = i.strip()
            num, colour = i_clean.split(" ")
            match colour:
                case "blue":
                    if int(num) > max_blue:
                        return False
                case "red":
                    if int(num) > max_red:
                        return False
                case "green":
                    if int(num) > max_green:
                        return False
                case _:
                    assert NotImplementedError("Should not reach this point")
    return True


def puzzle(puzzle_input: Any) -> Any:
    total = 0
    for game in puzzle_input:
        game_info, balls = game.split(": ")
        game_number = int(game_info.replace("Game ", ""))

        ball_split = balls.split(";")
        if inner_ball_check(ball_split):
            total += game_number

    return total


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
        puzzle_input_r: list[str] = [x.rstrip() for x in puzzle_input]
        # puzzle_input_r: list[int] = [int(x.rstrip()) for x in puzzle_input]
        print(puzzle(puzzle_input_r))

    else:
        puzzle_input: list[str] = open(f"{dir_path}/test.txt", "r").readlines()
        puzzle_input_r: list[str] = [x.rstrip() for x in puzzle_input]
        # puzzle_input_r: list[int] = [int(x.rstrip()) for x in puzzle_input]
        assert puzzle(puzzle_input_r) == 8

    if clock:
        print("time: ", time.time() - start)  # type: ignore

    if file:
        sys.stdout = orig_stdout  # type: ignore
        f.close()  # type: ignore
