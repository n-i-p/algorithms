# https://codeforces.com/problemset/problem/1/B


def toint(s):
    ret = 0
    for x, c in enumerate(reversed(s)):
        ret += (26 ** x) * (ord(c) - ord('A') + 1)
    return ret


def tostr(n):
    ret = []
    while n > 0:
        v = chr(n % 26 + ord('A') - 1)
        if v == '@':
            v = 'Z'
            n -= 1
        ret.append(v)
        n //= 26
    return ''.join(reversed(ret))


def func_sol(raw_data):
    import re
    solutions = []
    rerc = re.compile('R([0-9]+)C([0-9]+)')
    rexy = re.compile('([A-Z]+)([0-9]+)')
    for cell in raw_data.split('\n')[1:-1]:
        match = rerc.fullmatch(cell)
        if match is not None:
            nr = int(match.group(1))
            nc = int(match.group(2))
            solutions.append(f'{tostr(nc)}{nr}')
            continue
        match = rexy.fullmatch(cell)
        if match is not None:
            sc = match.group(1)
            nr = int(match.group(2))
            solutions.append(f'R{nr}C{toint(sc)}')
            continue
        raise NotImplementedError()
    return '\n'.join(solutions)


def main():
    try:
        from codeforces.utilities import run_tests
        run_tests(func_sol)
    except ImportError:
        from sys import stdin
        print(func_sol(stdin.read()))


main()
