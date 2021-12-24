# Solution can be done using numpy
import numpy as np

matrix = np.zeros((1000, 1000))


# turn on 0,0 through 999,999
def turn(command: str, start: tuple, end: tuple):
    global matrix
    start_x, start_y = start
    end_x, end_y = end

    for x in range(start_x, end_x + 1):
        for y in range(start_y, end_y + 1):
            if command == "on":
                matrix[x][y] += 1
            else:
                matrix[x][y] = max(0, matrix[x][y] - 1)


def toggle(start: tuple, end: tuple):
    global matrix
    start_x, start_y = start
    end_x, end_y = end

    for x in range(start_x, end_x + 1):
        for y in range(start_y, end_y + 1):
            matrix[x][y] += 2


puzzle_input = open("input.txt", "r").readlines()
for line in puzzle_input:

    if "toggle" in line:
        line = line.replace("toggle ", "")
        start, end = line.split(" through ")
        start = tuple(map(int, start.split(",")))
        end = tuple(map(int, end.split(",")))
        toggle(start, end)

    else:
        line = line.replace("turn ", "")
        line = line.replace(" through ", " ")
        command, start, end = line.split(" ")
        start = tuple(map(int, start.split(",")))
        end = tuple(map(int, end.split(",")))
        turn(command, start, end)

print(matrix.sum())
