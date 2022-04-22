import math


def count_a_b_c(n):
    ans = 0
    for a in range(1, n + 1):
        if a * a * a > n:
            break

        for b in range(a, n + 1):
            if b * b > n:
                break
            c = n // (a * b)
            if c < b:
                break

            ans += c - b + 1

    return ans


if __name__ == '__main__':
    n = int(input())
    print(count_a_b_c(n))
