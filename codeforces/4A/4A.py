# https://codeforces.com/problemset/problem/?/?

def func_sol(raw_data):
    w = int(raw_data)
    return 'YES' if w % 2 == 0 and w > 2 else 'NO'


def main():
    try:
        from codeforces.utilities import run_tests
        run_tests(func_sol)
    except ImportError:
        from sys import stdin
        print(func_sol(stdin.read()))


main()
