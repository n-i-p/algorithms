# https://codeforces.com/problemset/problem/29/A

def func_sol(raw_data):
    camels = [list(map(int, line.split(' '))) for line in raw_data.split('\n')[1:-1]]
    n = len(camels)
    for i in range(0, n - 1):
        for j in range(i, n):
            if camels[i][1] == - camels[j][1]:
                if abs(camels[i][0] - camels[j][0]) == abs(camels[j][1]):
                    return "YES"
    return "NO"


def main():
    try:
        from codeforces.utilities import run_tests
        run_tests(func_sol)
    except ImportError:
        from sys import stdin
        print(func_sol(stdin.read()))


main()
