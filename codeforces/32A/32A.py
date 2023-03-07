# https://codeforces.com/problemset/problem/32/A

def func_sol(raw_data):
    lines = raw_data.split('\n')
    n, d = map(int, lines[0].split(' '))
    a = list(map(int, lines[1].split(' ')))
    nr = 0
    for i in range(n):
        for j in range(n):
            if abs(a[i] - a[j]) <= d and i != j:
                nr += 1
    return str(nr)


def main():
    try:
        from codeforces.utilities import run_tests
        run_tests(func_sol)
    except ImportError:
        from sys import stdin
        print(func_sol(stdin.read()))


main()
