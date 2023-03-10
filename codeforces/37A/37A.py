# https://codeforces.com/problemset/problem/37/A

def func_sol(lines):
    f = [0] * 1001
    n = int(lines[0])
    a = list(map(int, lines[1].split(' ')))
    for e in a:
        f[e] += 1
    return str(max(f)) + ' ' + str(len([e for e in f if e != 0]))


def main():
    try:
        from codeforces.utilities import run_tests
        run_tests(func_sol)
    except ImportError:
        from sys import stdin
        print(func_sol(stdin.read().split('\n')[:-1]))


main()
