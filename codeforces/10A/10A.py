# https://codeforces.com/problemset/problem/10/A

def func_sol(raw_data):
    lines = raw_data.split('\n')[:-1]
    n, p1, p2, p3, t1, t2 = list(map(int, lines[0].split(' ')))
    periods = [list(map(int, line.split(' '))) for line in lines[1:]]

    total_power = 0
    last_timestamp = periods[0][0]
    for period in periods:
        total_power += (period[1] - period[0]) * p1
        afk = period[0] - last_timestamp
        if afk > 0:
            total_power += min(t1, afk) * p1
            afk -= min(t1, afk)
        if afk > 0:
            total_power += min(t2, afk) * p2
            afk -= min(t2, afk)
        if afk > 0:
            total_power += afk * p3
        last_timestamp = period[1]

    return str(total_power)


def main():
    try:
        from codeforces.utilities import run_tests
        run_tests(func_sol)
    except ImportError:
        from sys import stdin
        print(func_sol(stdin.read()))


main()
