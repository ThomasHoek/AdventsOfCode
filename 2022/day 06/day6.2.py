
def puzzle(puzzle_input: str) -> int:
    """
    puzzle Day 6

    Finds in a chunksize of 4 (predetermined), if no duplicate letters appear

    Args:
        puzzle_input (str): input string

    Returns:
        int: index
    """

    # check if type is correct
    if type(puzzle_input) != str:
        raise TypeError("Input needs to be a string")

    buffer_size = 14

    for i in range(0, len(puzzle_input)):
        buffer = puzzle_input[i:i+buffer_size]

        if len(set(buffer)) > 13:
            return i + buffer_size

    # wrong value
    return -1


if __name__ == "__main__":
    import sys
    import os

    try:
        test = sys.argv[1] == "test"
    except IndexError:
        test = False

    dir_path = os.path.dirname(os.path.realpath(__file__))
    if test:
        puzzle_input = open(f"{dir_path}/test.txt", "r").readlines()
        puzzle_input = [x.rstrip() for x in puzzle_input]
        assert puzzle(puzzle_input[0]) == 19
        assert puzzle(puzzle_input[1]) == 23
        assert puzzle(puzzle_input[2]) == 23
        assert puzzle(puzzle_input[3]) == 29
        assert puzzle(puzzle_input[4]) == 26
        print("TEST passed")
        exit(0)

    else:
        puzzle_input = open(f"{dir_path}/input.txt", "r").readlines()
        puzzle_input = [x.rstrip() for x in puzzle_input]
        print(puzzle(puzzle_input[0]))
