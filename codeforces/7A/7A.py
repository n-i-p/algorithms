# https://codeforces.com/problemset/problem/7/A

def func_sol(raw_data):
    lines = raw_data.split('\n')[:-1]
    count = 0
    for i in range(8):
        line = True
        column = True
        for j in range(8):
            if lines[i][j] == 'W':
                line = False
            if lines[j][i] == 'W':
                column = False
        if line:
            count += 1
        if column:
            count += 1
    return str(count if count < 16 else 8)


def main():
    try:
        from codeforces.utilities import run_tests
        run_tests(func_sol)
    except ImportError:
        from sys import stdin
        print(func_sol(stdin.read()))


main()
