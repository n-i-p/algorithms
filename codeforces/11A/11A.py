# https://codeforces.com/problemset/problem/11/A

def func_sol(raw_data):
    n_d, b = raw_data.split('\n')[:-1]
    n, d = map(int, n_d.split(' '))
    b = list(map(int, b.split(' ')))
    nr = 0
    for i in range(1, len(b)):
        diff = b[i] - b[i - 1]
        if diff > 0:
            continue
        diff = abs(diff) + 1
        t = (diff + (d - 1)) // d
        b[i] += d * t
        nr += t
    return str(nr)


def main():
    try:
        from codeforces.utilities import run_tests
        run_tests(func_sol)
    except ImportError:
        from sys import stdin
        print(func_sol(stdin.read()))


main()
