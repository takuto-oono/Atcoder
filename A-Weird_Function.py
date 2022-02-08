def f(x: int) -> int:
    return x * x + 2 * x + 3


def main_cal(t: int) -> int:
    return f(f(f(t) + t) + f(f(t)))


if __name__ == '__main__':
    t = int(input())
    print(main_cal(t))
