# https://codeforces.com/problemset/problem/15/A

def func_sol(raw_data):
    data = raw_data.split('\n')[:-1]
    n, t = map(int, data[0].split(' '))
    flatville = [list(map(int, house.split(' '))) for house in data[1:]]
    flatville.sort(key=lambda house: house[0] - house[1] / 2)

    center, length = flatville[0]
    last_wall = center + length / 2
    pp = 2  # before first + after last
    for center, length in flatville[1:]:
        left_wall = center - length / 2
        right_wall = center + length / 2
        if left_wall - last_wall == t:
            pp += 1
        elif left_wall - last_wall > t:
            pp += 2
        last_wall = right_wall

    return str(pp) + '\n'


def main():
    try:
        from codeforces.utilities import run_tests
        run_tests(func_sol)
    except ImportError:
        from sys import stdin
        print(func_sol(stdin.read()))


main()
