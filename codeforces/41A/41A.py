# https://codeforces.com/problemset/problem/41/A

def func_sol(lines):
    return str("YES" if lines[0] == lines[1][::-1] else "NO")


def main():
    try:
        from codeforces.utilities import run_tests
        run_tests(func_sol)
    except ImportError:
        from sys import stdin
        print(func_sol(stdin.read().split('\n')[:-1]))


main()
