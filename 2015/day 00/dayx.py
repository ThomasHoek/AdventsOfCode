def puzzle(puzzle_input):
    pass


if __name__ == "__main__":
    import sys
    import os

    try:
        final: bool = sys.argv[1] == "final"
    except IndexError:
        final: bool = False

    dir_path: str = os.path.dirname(os.path.realpath(__file__))

    if final:
        puzzle_input: list[str] = open(f"{dir_path}/input.txt",
                                       "r").readlines()
        puzzle_input: list[str] = [x.rstrip() for x in puzzle_input]
        print(puzzle(puzzle_input))

    else:
        puzzle_input: list[str] = open(f"{dir_path}/test.txt",
                                       "r").readlines()
        puzzle_input: list[str] = [x.rstrip() for x in puzzle_input]
        assert puzzle(puzzle_input) == NotImplemented
        exit(0)
