# https://codeforces.com/problemset/problem/40/A
import math


def func_sol(lines):
    x, y = map(int, lines[0].split(' '))
    if x == 0 or y == 0:
        return 'black'
    z = math.sqrt(x ** 2 + y ** 2)
    if x > 0 and y > 0 or x < 0 and y < 0:
        if float(int(z)) == z:
            return 'black'
        if int(z) % 2 == 0:
            return 'black'
        return 'white'
    else:
        if float(int(z)) == z:
            return 'black'
        if int(z) % 2 == 0:
            return 'white'
        return 'black'
    raise NotImplementedError()


def main():
    try:
        from codeforces.utilities import run_tests
        run_tests(func_sol)
    except ImportError:
        from sys import stdin
        print(func_sol(stdin.read().split('\n')[:-1]))


main()
