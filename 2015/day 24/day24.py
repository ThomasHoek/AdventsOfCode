from copy import deepcopy
from typing import Any
from dataclasses import dataclass


@dataclass
class int_str:
    number: int
    collected_str: str
    str_len: int


min_n: float = float("inf")
all_a_perm: set[str] = set()


def recursive_solution(subset: list[int],
                       n: int,
                       a: int_str,
                       b: int_str,
                       c: int_str,
                       key_dict: dict[str, bool]) -> dict[str, bool]:

    # # already exists
    # if a.collected_str in key_dict or b.collected_str in key_dict or c.collected_str in key_dict:
    #     return True  # type: ignore

    # smaller than 0, a b c
    if a.number < 0 or b.number < 0 or c.number < 0:
        return False  # type: ignore

    # if equal
    if a.number == 0 and b.number == 0 and c.number == 0:
        key_dict[a.collected_str] = True
        key_dict[b.collected_str] = True
        key_dict[c.collected_str] = True

        # min_n = min(a.collected_str.count("_"), b.collected_str.count("_"), c.collected_str.count("_"), min_n)
        return True  # type: ignore

    # if N too small
    if n < 0:
        # print("N smaller than 0")
        return False  # type: ignore

    # A
    # if a != 0:

    new_a: int_str = int_str(a.number - subset[n],
                             a.collected_str + "_" + str(subset[n]),
                             a.str_len + 1)
    recursive_solution(subset, n - 1, new_a, b, c, key_dict)

    # B
    # if b != 0:s
    new_b: int_str = int_str(b.number - subset[n],
                             b.collected_str + "_" + str(subset[n]),
                             b.str_len + 1)
    recursive_solution(subset, n - 1, a, new_b, c, key_dict)

    # C
    # if a != 0 and b != 0:
    new_c: int_str = int_str(c.number - subset[n],
                             c.collected_str + "_" + str(subset[n]),
                             c.str_len + 1)
    recursive_solution(subset, n - 1, a, b, new_c, key_dict)

    # print(boola, boolb, boolc)
    return key_dict


def puzzle(puzzle_input: list[int]) -> Any:

    if (len(puzzle_input) < 3):
        raise AttributeError

    key_dict: dict[str, bool] = dict()

    puzzle_input.reverse()
    if sum(puzzle_input) % 3 == 0:

        abc = int_str(int(sum(puzzle_input) / 3), "", 0)
        key_dict = recursive_solution(puzzle_input,
                                      n=len(puzzle_input) - 1,
                                      a=deepcopy(abc),
                                      b=deepcopy(abc),
                                      c=deepcopy(abc),
                                      key_dict=key_dict)

    assert type(key_dict) == dict

    
    # # all different permutations for A
    combos: list[list[int]] = [
        [int(x2) for x2 in x.split("_")[1:]] for x in list(key_dict.keys())]

    print(combos)
    
    # # find shortest through min
    # len_combos = list(map(len, combos))
    # minimum: int = min(len_combos)
    # indices: list[int] = [i for i, v in enumerate(len_combos) if v == minimum]
    # short_lst = []
    # for i in indices:
    #     short_lst.append(combos[i])

    # print(short_lst)


if __name__ == "__main__":
    import sys
    import os
    from io import TextIOWrapper
    from typing import TextIO

    try:
        final: bool = "final" in sys.argv
        file: bool = "file" in sys.argv

    except IndexError:
        final: bool = False
        file: bool = False

    dir_path: str = os.path.dirname(os.path.realpath(__file__))

    if file:
        orig_stdout: TextIO = sys.stdout
        f: TextIOWrapper = open('out.txt', 'w')
        sys.stdout = f

    if final:
        puzzle_input: list[str] = open(f"{dir_path}/input.txt",
                                       "r").readlines()
        puzzle_input_r: list[int] = [int(x.rstrip()) for x in puzzle_input]
        print(puzzle(puzzle_input_r))

    else:
        puzzle_input: list[str] = open(f"{dir_path}/test.txt",
                                       "r").readlines()
        puzzle_input_r: list[int] = [int(x.rstrip()) for x in puzzle_input]
        puzzle(puzzle_input_r)
        # assert puzzle(puzzle_input) == NotImplemented

    if file:
        sys.stdout = orig_stdout  # type: ignore
        f.close()   # type: ignore
