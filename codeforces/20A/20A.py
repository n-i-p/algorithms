# https://codeforces.com/problemset/problem/20/A
import re


def func_sol(raw_data):
    data = re.sub('/+', '/', raw_data.strip())
    if len(data) > 1 and data[-1] == '/':
        return data[:-1]
    return data


def main():
    try:
        from codeforces.utilities import run_tests
        run_tests(func_sol)
    except ImportError:
        from sys import stdin
        print(func_sol(stdin.read()))


main()
