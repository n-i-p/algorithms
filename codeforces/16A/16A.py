# https://codeforces.com/problemset/problem/16/A

def func_sol(raw_data):
    data = raw_data.split('\n')[:-1]
    n, m = map(int, data[0].split(' '))
    lines = data[1:]
    for line in lines:
        for c in line:
            if c != line[0]:
                return "NO\n"
    for i in range(len(lines) - 1):
        if lines[i][0] == lines[i + 1][0]:
            return "NO\n"
    return "YES\n"


def main():
    try:
        from codeforces.utilities import run_tests
        run_tests(func_sol)
    except ImportError:
        from sys import stdin
        print(func_sol(stdin.read()))


main()
