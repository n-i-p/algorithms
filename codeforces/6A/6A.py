# https://codeforces.com/problemset/problem/6/A

def check(x, y, z):
    if x + y > z and y + z > x and z + x > y:
        return 2
    if x + y == z or y + z == x or z + x == y:
        return 1
    return 0


def func_sol(raw_data):
    numbers = list(map(int, raw_data.strip().split()))
    solutions = ['IMPOSSIBLE', 'SEGMENT', 'TRIANGLE']
    sol_idx = 0
    length = len(numbers)
    for a in range(length - 2):
        for b in range(a + 1, length - 1):
            for c in range(b + 1, length):
                sol_tmp = check(numbers[a], numbers[b], numbers[c])
                sol_idx = max(sol_idx, sol_tmp)

    return str(solutions[sol_idx])


def main():
    try:
        from codeforces.utilities import run_tests
        run_tests(func_sol)
    except ImportError:
        from sys import stdin
        print(func_sol(stdin.read()))


main()
