def judge(x: int, a: int, d: int, n: int) -> int:
    last = a + d * (n - 1)
    if d >= 0:
        if x <= a:
            return a - x
        if x >= last:
            return x - last

    if d < 0:
        if x >= a:
            return x - a
        if x <= last:
            return last - x

    for i in range(10 ** 6 + 1):
        if (x + i - a) % abs(d) == 0:
            return i

        if (x - i - a) % abs(d) == 0:
            return i


def main():
    x, a, d, n = map(int, input().split())
    print(judge(x, a, d, n))


if __name__ == '__main__':
    main()
