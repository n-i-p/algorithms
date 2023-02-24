# https://codeforces.com/problemset/problem/19/A

def func_sol(raw_data):
    lines = raw_data.split('\n')

    n = int(lines[0])

    standings = dict([(team, [0, 0, 0]) for team in lines[1:1 + n]])

    for line in lines[1 + n:-1]:
        raw_names, raw_goals = line.split(' ')

        team0, team1 = raw_names.split('-')
        goals0, goals1 = list(map(int, raw_goals.split(':')))

        if goals0 == goals1:
            standings[team0][0] += 1
            standings[team1][0] += 1
        elif goals0 > goals1:
            standings[team0][0] += 3
        elif goals0 < goals1:
            standings[team1][0] += 3

        # scored
        standings[team0][1] += goals0
        standings[team1][1] += goals1

        # missed
        standings[team0][2] += goals1
        standings[team1][2] += goals0

    sorted_standings = sorted(
        list(standings.items()),
        key=lambda e: (-e[1][0], -(e[1][1] - e[1][2]), -e[1][1]),
    )

    solution = [e[0] for e in sorted_standings[:n // 2]]

    return str('\n'.join(sorted(solution)))


def main():
    try:
        from codeforces.utilities import run_tests
        run_tests(func_sol)
    except ImportError:
        from sys import stdin
        print(func_sol(stdin.read()))


main()
