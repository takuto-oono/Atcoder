import math
a_list = []
prime_factor_list = []


def create_prime_factor_list():
    prime_factors = []
    for i in range(len(a_list)):
        a = a_list[i]
        if a % 2 == 0:
            prime_factors.append(2)
            while(a % 2 == 0):
                a //= 2
        print(a)
        if a == 1:
            continue

        for prime in range(3, a + 1, 2):
            print(i, prime)
            if a % prime == 0:
                prime_factors.append(prime)
                while(a % prime == 0):
                    a //= prime

            if a == 1:
                break
    print(prime_factors)
    prime_factors = list(set(prime_factors))
    prime_factor_list = prime_factors


def print_ans(m):
    print(prime_factor_list)
    x = 1
    for prime in prime_factor_list:
        x *= prime

    for ans in range(1, m + 1):
        if math.gcd(ans, x) == 1:
            print(ans)


if __name__ == '__main__':
    n, m = map(int, input().split())
    prime_factor_list = [1]
    a_list = list(map(int, input().split()))
    create_prime_factor_list()
    print_ans(m)
