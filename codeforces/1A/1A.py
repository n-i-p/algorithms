# https://codeforces.com/problemset/problem/1/A

def func_sol(raw_data):
    n, m, a = map(int, raw_data.split())
    x = (n + a - 1) // a
    y = (m + a - 1) // a
    z = x * y
    return str(z)


def main():
    try:
        from codeforces.utilities import run_tests
        run_tests(func_sol)
    except ImportError:
        from sys import stdin
        print(func_sol(stdin.read()))


main()
