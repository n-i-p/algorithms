# https://codeforces.com/problemset/problem/27/A

def func_sol(raw_data):
    a = list(map(int, raw_data.split('\n')[1].split(' ')))
    x = [False] * 3002
    for e in a:
        x[e] = True
    for i in range(1, 3002):
        if not x[i]:
            return str(i)
    raise NotImplementedError()


def main():
    try:
        from codeforces.utilities import run_tests
        run_tests(func_sol)
    except ImportError:
        from sys import stdin
        print(func_sol(stdin.read()))


main()
