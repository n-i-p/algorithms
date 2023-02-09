# https://codeforces.com/problemset/problem/2/B
from sys import getsizeof


def tz_ld(n):
    # Trailing Zeros, Last Digit
    if n == 0:
        return 1, 0
    zeros = 0
    while n % 10 == 0:
        zeros += 1
        n //= 10
    return zeros, n % 10


def func_sol(raw_data):
    lines = raw_data.split('\n')

    N = int(lines[0])
    A = []
    for temp in lines[1:-1]:
        A.append(list(map(int, temp.split(' '))))

    # print(N)
    # print('\n'.join([' '.join(map(str, l)) for l in A]))

    T = [[-1] * N for _ in range(N)]  # Trailing Zeros
    L = [[-1] * N for _ in range(N)]  # Last Digit
    D = [[-1] * N for _ in range(N)]  # Direction

    PRIORITIES = [1, 3, 7, 9, 4, 6, 8, 2, 5, 0]
    for X in range(N - 1, -1, -1):
        for Y in range(N - 1, -1, -1):
            # print(X, Y)
            if X == N - 1 and Y == N - 1:
                T[X][Y], L[X][Y] = tz_ld(A[X][Y])
            elif X == N - 1:
                tz, ld = tz_ld(L[X][Y + 1] * A[X][Y])
                D[X][Y] = 'R'
                T[X][Y], L[X][Y] = T[X][Y + 1] + tz, ld
            elif Y == N - 1:
                tz, ld = tz_ld(L[X + 1][Y] * A[X][Y])
                D[X][Y] = 'D'
                T[X][Y], L[X][Y] = T[X + 1][Y] + tz, ld
            else:
                if T[X][Y + 1] == T[X + 1][Y]:
                    _, ldR = tz_ld(L[X][Y + 1] * A[X][Y])
                    _, ldD = tz_ld(L[X + 1][Y] * A[X][Y])
                    if PRIORITIES.index(ldR) <= PRIORITIES.index(ldD):
                        nX, nY, d = X, Y + 1, 'R'
                    else:
                        nX, nY, d = X + 1, Y, 'D'
                elif T[X][Y + 1] < T[X + 1][Y]:
                    nX, nY, d = X, Y + 1, 'R'
                elif T[X][Y + 1] > T[X + 1][Y]:
                    nX, nY, d = X + 1, Y, 'D'
                else:
                    raise NotImplementedError()

                tz, ld = tz_ld(L[nX][nY] * A[X][Y])
                D[X][Y] = d
                T[X][Y], L[X][Y] = T[nX][nY] + tz, ld

    # print('\n'.join([' '.join(map(str, l)) for l in L]))
    # print('\n'.join([' '.join(map(str, l)) for l in T]))
    # print('\n'.join([' '.join(map(str, l)) for l in D]))

    directions = []
    X, Y = 0, 0
    while X != N - 1 or Y != N - 1:
        directions.append(D[X][Y])
        if D[X][Y] == 'R':
            Y += 1
        elif D[X][Y] == 'D':
            X += 1
        elif D[X][Y] == -1:
            break
        else:
            raise NotImplementedError()

    return str(T[0][0]) + '\n' + ''.join(directions)


def main():
    try:
        from codeforces.utilities import run_tests
        run_tests(func_sol)
    except ImportError:
        from sys import stdin
        print(func_sol(stdin.read()))


main()
