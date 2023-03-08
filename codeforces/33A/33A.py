# https://codeforces.com/problemset/problem/33/A

def func_sol(raw_data):
    lines = raw_data.split('\n')[:-1]
    n, m, k = map(int, lines[0].split(' '))
    data = [list(map(int, line.split(' '))) for line in lines[1:]]
    rows = {}
    for row, viability in data:
        rows[row] = min(rows.get(row, viability), viability)
    return str(min(k, sum(rows.values())))


def main():
    try:
        from codeforces.utilities import run_tests
        run_tests(func_sol)
    except ImportError:
        from sys import stdin
        print(func_sol(stdin.read()))


main()
