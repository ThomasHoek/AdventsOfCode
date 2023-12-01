import os
import copy


dir_path: str = os.path.dirname(os.path.realpath(__file__))
print(dir_path)
puzzle_input = int(open(f"{dir_path}/../../input.txt", "r").readline())


def prime_sieve(n: int) -> list[int]:
    long_arr: list[int] = [1] * (n)
    max_range: int = round(n**0.5)
    i = 2
    while i < (max_range):
        if long_arr[i] != 0:
            for j in range(i, n, i):
                long_arr[j] = 0
            long_arr[i] = 1
        i += 1
    return [i for i, x in enumerate(long_arr) if x][2:]


def prime_factor(n: int) -> list[int]:
    global prime_lst
    prime_counter: int = 0
    i: int = 2
    factor_lst: list[int] = []

    while (i <= n - 1):
        if (n % i == 0):
            factor_lst.append(i)
            n = n // i
        else:
            prime_counter += 1
            i = prime_lst[prime_counter]

    factor_lst.append(i)
    return factor_lst


# group [2,2,3] into [(2,2), (3,1)]
def group_lst(n: int) -> list[tuple[int, int]]:
    lst: list[int] = prime_factor(n)
    set_x = set(lst)
    return [(num, lst.count(num)) for num in set_x]


def new_sum(n: int) -> int:
    """https://en.wikipedia.org/wiki/Divisor_function"""
    prime_list: list[tuple[int, int]] = group_lst(n)
    sum = 1

    for i in prime_list:
        upper: int = i[0] ** (i[1] + 1) - 1
        lower: int = i[0] - 1

        sum *= int(upper / lower)

    return sum * 10


counter: int = 2
# Dynamic search list
prime_lst: list[int] = prime_sieve(puzzle_input)
print("primes done")
while True:
    presents: int = new_sum(counter)
    # print(counter, presents)
    if presents > puzzle_input:
        print(counter)
        break
    counter += 1

    if counter % 100_000 == 0:
        break
        # print(counter)
