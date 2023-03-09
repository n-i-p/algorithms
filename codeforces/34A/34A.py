# https://codeforces.com/problemset/problem/34/A

def func_sol(raw_data):
    lines = raw_data.split('\n')[:-1]
    n = int(lines[0])
    a = list(map(int, lines[1].split(' ')))
    min_diff = abs(a[0] - a[1])
    x, y = 0, 1
    for idx in range(0, n):
        temp_min_diff = abs(a[idx] - a[(idx + 1) % n])
        if temp_min_diff < min_diff:
            min_diff = temp_min_diff
            x, y = idx, (idx + 1) % n
    return str(x + 1) + ' ' + str(y + 1)


def main():
    try:
        from codeforces.utilities import run_tests
        run_tests(func_sol)
    except ImportError:
        from sys import stdin
        print(func_sol(stdin.read()))


main()
