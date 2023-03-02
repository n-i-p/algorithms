# https://codeforces.com/problemset/problem/26/A

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
    n = int(raw_data.strip())

    primes = []
    for d in prime_numbers():
        if d > n:
            break
        primes.append(d)

    cnt = 0
    for i in range(len(primes) - 1):
        for j in range(i + 1, len(primes)):
            ci = 1
            while primes[i] ** ci <= n:
                cj = 1
                while primes[j] ** cj <= n:
                    t = primes[i] ** ci * primes[j] ** cj
                    if t <= n:
                        cnt += 1
                    cj += 1
                ci += 1

    return str(cnt)


def main():
    try:
        from codeforces.utilities import run_tests
        run_tests(func_sol)
    except ImportError:
        from sys import stdin
        print(func_sol(stdin.read()))


main()
