# https://codeforces.com/problemset/problem/31/A

def func_sol(raw_data):
    a = list(map(int, raw_data.split('\n')[1].split(' ')))
    n = len(a)
    for i in range(n):
        for j in range(n):
            for k in range(n):
                if a[i] == a[j] + a[k] and i != j and j != k and k != i:
                    return f'{i + 1} {j + 1} {k + 1}'
    return str(-1)


def main():
    try:
        from codeforces.utilities import run_tests
        run_tests(func_sol)
    except ImportError:
        from sys import stdin
        print(func_sol(stdin.read()))


main()
