# https://codeforces.com/problemset/problem/22/A

def func_sol(raw_data):
    data = raw_data.split('\n')[:-1]
    n = int(data[0])
    v = list(map(int, data[1].split(' ')))

    idx = 0
    min1st = v[idx]

    min2nd = None
    for idx in range(1, n):
        if min1st != v[idx]:
            min2nd = v[idx]
            break
    if min2nd is None:
        return "NO"

    min1st, min2nd = min(min1st, min2nd), max(min1st, min2nd)
    for idx in range(idx + 1, n):
        if v[idx] < min1st:
            min2nd = min1st
            min1st = v[idx]
        elif min1st < v[idx] < min2nd:
            min2nd = v[idx]

    return str(min2nd)


def main():
    try:
        from codeforces.utilities import run_tests
        run_tests(func_sol)
    except ImportError:
        from sys import stdin
        print(func_sol(stdin.read()))


main()
