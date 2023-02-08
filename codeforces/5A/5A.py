# https://codeforces.com/problemset/problem/5/A

def func_sol(raw_data):
    lines = raw_data.split('\n')
    length = 0
    persons = 0
    for line in lines[:-1]:
        if line[0] == '+':
            persons += 1
        elif line[0] == '-':
            persons -= 1
        else:
            length += len(line.split(':')[1]) * persons
    return str(length)


def main():
    try:
        from codeforces.utilities import run_tests
        run_tests(func_sol)
    except ImportError:
        from sys import stdin
        print(func_sol(stdin.read()))


main()
