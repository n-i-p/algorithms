# https://codeforces.com/problemset/problem/8/A

def check(full, first, second):
    pos_first = 0
    while pos_first != -1:
        pos_first = full.find(first)
        if pos_first == -1:
            break
        pos_second = full[pos_first + len(first):].find(second)
        if pos_second != -1:
            return True
        full = full[pos_first + 1:]
    return False


def func_sol(raw_data):
    full, first, second, _ = raw_data.split('\n')
    rfull = full[::-1]

    forward = check(full, first, second)
    backward = check(rfull, first, second)

    if forward and backward:
        return "both"
    elif forward:
        return "forward"
    elif backward:
        return "backward"
    else:
        return "fantasy"


def main():
    try:
        from codeforces.utilities import run_tests
        run_tests(func_sol)
    except ImportError:
        from sys import stdin
        print(func_sol(stdin.read()))


main()
