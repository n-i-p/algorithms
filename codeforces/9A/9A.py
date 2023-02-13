# https://codeforces.com/problemset/problem/9/A

def func_sol(raw_data):
    return str(['0/1', '1/1', '5/6', '2/3', '1/2', '1/3', '1/6'][max(map(int, raw_data.split()))])


def main():
    try:
        from codeforces.utilities import run_tests
        run_tests(func_sol)
    except ImportError:
        from sys import stdin
        print(func_sol(stdin.read()))


main()
