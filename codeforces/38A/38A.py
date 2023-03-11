# https://codeforces.com/problemset/problem/38/A

def func_sol(lines):
    n = int(lines[0])
    d = [0, 0] + list(map(int, lines[1].split(' ')))
    a, b = map(int, lines[2].split(' '))
    y = sum([d[r] for r in range(a + 1, b + 1)])
    return str(y)


def main():
    try:
        from codeforces.utilities import run_tests
        run_tests(func_sol)
    except ImportError:
        from sys import stdin
        print(func_sol(stdin.read().split('\n')[:-1]))


main()
