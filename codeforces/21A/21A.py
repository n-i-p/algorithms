# https://codeforces.com/problemset/problem/21/A
import re


def func_sol(raw_data):
    match = re.fullmatch(
        pattern="([0-9A-Za-z_]{1,16})@(([0-9A-Za-z_]{1,16})(\\.[0-9A-Za-z_]{1,16})*)(\\/[0-9A-Za-z_]{1,16})?",
        string=raw_data.strip()
    )
    if match is None:
        return "NO"
    if 1 <= len(match.group(2)) <= 32:
        return "YES"
    return "NO"


def main():
    try:
        from codeforces.utilities import run_tests
        run_tests(func_sol)
    except ImportError:
        from sys import stdin
        print(func_sol(stdin.read()))


main()
