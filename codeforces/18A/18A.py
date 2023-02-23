# https://codeforces.com/problemset/problem/18/A

def sd(x1, y1, x2, y2):
    return (y2 - y1) ** 2 + (x2 - x1) ** 2


def is_right_triangle(x1, y1, x2, y2, x3, y3):
    s12 = sd(x1, y1, x2, y2)
    s23 = sd(x2, y2, x3, y3)
    s31 = sd(x3, y3, x1, y1)
    return (s12 + s23 == s31 or s23 + s31 == s12 or s31 + s12 == s23) \
        and s12 != 0 and s23 != 0 and s31 != 0


def func_sol(raw_data):
    x1, y1, x2, y2, x3, y3 = map(int, raw_data.split('\n')[0].split(' '))

    if is_right_triangle(x1, y1, x2, y2, x3, y3):
        return "RIGHT"

    dx = [-1, 0, 1, 0]
    dy = [0, 1, 0, -1]
    for p in range(3):
        for i in range(4):
            if is_right_triangle(
                    x1 + (dx[i] if p == 0 else 0),
                    y1 + (dy[i] if p == 0 else 0),
                    x2 + (dx[i] if p == 1 else 0),
                    y2 + (dy[i] if p == 1 else 0),
                    x3 + (dx[i] if p == 2 else 0),
                    y3 + (dy[i] if p == 2 else 0),
            ):
                return "ALMOST"

    return "NEITHER"


def main():
    try:
        from codeforces.utilities import run_tests
        run_tests(func_sol)
    except ImportError:
        from sys import stdin
        print(func_sol(stdin.read()))


main()
