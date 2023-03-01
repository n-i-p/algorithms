# https://codeforces.com/problemset/problem/23/A

def func_sol(raw_data):
    a = raw_data.strip()
    n = len(a)
    m = 0
    for l in range(n - 1, 0, -1):
        for s in range(0, n - l):
            if a[s:s + l] in a[s + 1:]:
                m = max(m, l)
    return str(m)


def main():
    try:
        from codeforces.utilities import run_tests
        run_tests(func_sol)
    except ImportError:
        from sys import stdin
        print(func_sol(stdin.read()))


main()
