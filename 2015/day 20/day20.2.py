import os
import copy
import itertools

dir_path = os.path.dirname(os.path.realpath(__file__))
print(dir_path)
puzzle_input = int(open(f"{dir_path}/input.txt", "r").readline())


def get_primes_to_max(n) -> list:
    long_arr = [1] * (n)
    max_range = round(n**0.5)
    i = 2
    while i < (max_range):
        if long_arr[i] != 0:
            for j in range(i, n, i):
                long_arr[j] = 0
            long_arr[i] = 1
        i += 1
    return [i for i, x in enumerate(long_arr) if x][2:]


def prime_factor(n):
    global prime_lst
    prime_counter = 0
    i = 2
    a = []
    while (i <= n - 1):
        if (n % i == 0):
            a.append(i)
            n = n // i
        else:
            prime_counter += 1
            i = prime_lst[prime_counter]

    a.append(i)
    return a


# group [2,2,3] into [(2,2), (3,1)]
def group_lst(n) -> list:
    lst = prime_factor(n)
    set_x = set(copy.deepcopy(lst))
    count_lst = []
    for num in set_x:
        count_lst.append([num ** x for x in range(0, lst.count(num) + 1)])
    return count_lst


def product_list(lst, cur):
    r = 1
    for x in lst:
        if (x * 50) >= cur:
            r *= x
    return r


def divisors(n) -> int:
    prime_lists = group_lst(n)
    lst = []
    for prod_lst in list(itertools.product(*prime_lists)):
        lst.append(product_list(prod_lst, n) * 11)
    return sum(lst)


# skip a bit
prime_lst = get_primes_to_max(29000000)
# counter = 500_000
# while True:
#     presents = int(divisors(counter))
#     if presents > puzzle_input:
#         print(counter)
#         break

#     if counter % 10000 == 0:
#         print(counter)

#     counter += 1

bigstep = True
counter = 500_000
while True:
    presents = divisors(counter)
    if presents > puzzle_input and not bigstep:
        print(counter)
        break

    elif presents > puzzle_input:
        bigstep = False
        counter -= int((counter / 10))   # back 10%

    if counter % 10000 == 0:
        print(counter)

    # add big skip tactic
    if bigstep:
        counter += 11
    else:
        counter += 1


# That's not the right answer; your answer is too high.
# If you're stuck, make sure you're using the full input data; there are also some general tips on the about page,
# or you can ask for hints on the subreddit. Please wait one minute before trying again. (You guessed 8437502.)
# higher
#1_320_000

# That's not the right answer.
# If you're stuck, make sure you're using the full input data;
# there are also some general tips on the about page, or you can ask for hints on the subreddit.
# Because you have guessed incorrectly 4 times on this puzzle,
# please wait 5 minutes before trying again. (You guessed 2097152.)


# 2_097_152
# 2_929_699
# 3_515_639
# 8_437_502
