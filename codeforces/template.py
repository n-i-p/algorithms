# https://codeforces.com/problemset/problem/?/?

def func_sol(lines):
    raise NotImplementedError()
    return str()


def main():
    try:
        from codeforces.utilities import run_tests
        run_tests(func_sol)
    except ImportError:
        from sys import stdin
        print(func_sol(stdin.read().split('\n')[:-1]))


main()
