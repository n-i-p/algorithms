# https://codeforces.com/problemset/problem/14/A

def func_sol(raw_data):
    data = raw_data.split('\n')
    n, m = map(int, data[0].split(' '))
    a = data[1:-1]

    x1, y1 = None, None
    for i in range(n):
        for j in range(m):
            if a[i][j] != '.':
                x1, y1 = i, j
                break
        if x1 is not None:
            break

    x2, y2 = None, None
    for j in range(m):
        for i in range(n):
            if a[i][j] != '.':
                x2, y2 = i, j
                break
        if x2 is not None:
            break

    tlx, tly = min(x1, x2), min(y1, y2)

    x1, y1 = None, None
    for i in range(n - 1, -1, -1):
        for j in range(m - 1, -1, -1):
            if a[i][j] != '.':
                x1, y1 = i, j
                break
        if x1 is not None:
            break

    x2, y2 = None, None
    for j in range(m - 1, -1, -1):
        for i in range(n - 1, -1, -1):
            if a[i][j] != '.':
                x2, y2 = i, j
                break
        if x2 is not None:
            break

    brx, bry = max(x1, x2), max(y1, y2)

    s = [a[i][tly:bry + 1] for i in range(tlx, brx + 1)]

    return '\n'.join(s) + '\n'


def main():
    try:
        from codeforces.utilities import run_tests
        run_tests(func_sol)
    except ImportError:
        from sys import stdin
        print(func_sol(stdin.read()))


main()
