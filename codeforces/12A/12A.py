# https://codeforces.com/problemset/problem/12/A

def func_sol(raw_data):
    a = raw_data.split('\n')[:-1]
    n = len(a)
    for i in range(n):
        for j in range(i + 1):
            if a[i][j] != a[n - i - 1][n - j - 1]:
                return "NO"
    return "YES"


def main():
    try:
        from codeforces.utilities import run_tests
        run_tests(func_sol)
    except ImportError:
        from sys import stdin
        print(func_sol(stdin.read()))


main()
