# https://codeforces.com/problemset/problem/30/A

def func_sol(raw_data):
    a, b, n = map(int, raw_data.split('\n')[0].split(' '))
    if a == 0:
        if b == 0:
            return str(5)
        return "No solution"
    if b % a != 0:
        return "No solution"
    x = abs(int(b // a)) ** (1 / n)
    if abs(x - round(x)) < 1e-6:
        x = round(x)
    if x - int(x) != 0:
        return "No solution"
    if int(x ** n) == int(b // a):
        return str(int(x))
    elif int((-x) ** n) == int(b // a):
        return str(int(-x))
    return "No solution"


def main():
    try:
        from codeforces.utilities import run_tests
        run_tests(func_sol)
    except ImportError:
        from sys import stdin
        print(func_sol(stdin.read()))


main()
