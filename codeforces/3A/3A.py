# https://codeforces.com/problemset/problem/3/A

def func_sol(raw_data):
    lines = raw_data.split('\n')[:-1]

    xs, ys = ord(lines[0][0]) - ord('a'), ord(lines[0][1]) - ord('1')
    xf, yf = ord(lines[1][0]) - ord('a'), ord(lines[1][1]) - ord('1')

    moves = []

    while xs != xf or ys != yf:
        if xs != xf and ys != yf:
            next_move = ('R' if xs < xf else 'L') + ('U' if ys < yf else 'D')
            xs += 1 if xs < xf else -1
            ys += 1 if ys < yf else -1
        elif xs == xf and ys != yf:
            next_move = 'U' if ys < yf else 'D'
            ys += 1 if ys < yf else -1
        elif xs != xf and ys == yf:
            next_move = 'R' if xs < xf else 'L'
            xs += 1 if xs < xf else -1
        elif xs == xf and ys == yf:
            break

        moves.append(next_move)

    return str(len(moves)) + '\n' + '\n'.join(moves)


def main():
    try:
        from codeforces.utilities import run_tests
        run_tests(func_sol)
    except ImportError:
        from sys import stdin
        print(func_sol(stdin.read()))


main()
