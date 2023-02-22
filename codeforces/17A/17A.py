# https://codeforces.com/problemset/problem/17/A


def is_prime(even_number):
    divisor = 3
    while divisor * divisor <= even_number:
        if even_number % divisor == 0:
            return False
        divisor += 2
    return True


def prime_numbers():
    yield 2
    n = 3
    while True:
        if is_prime(n):
            yield n
        n += 2


def func_sol(raw_data):
    n, k = map(int, raw_data.split('\n')[0].split(' '))

    solution = 0
    for i in range(2, n + 1):
        if not is_prime(i):
            continue
        goldbach = False
        pn = prime_numbers()
        a, b = next(pn), next(pn)
        while a <= i - 1:
            if a + b + 1 == i:
                goldbach = True
                break
            a, b = b, next(pn)
        if goldbach:
            solution += 1

    return str('YES' if solution >= k else 'NO')


def main():
    try:
        from codeforces.utilities import run_tests
        run_tests(func_sol)
    except ImportError:
        from sys import stdin
        print(func_sol(stdin.read()))


main()
