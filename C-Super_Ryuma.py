def count_min_operation(x1: int, y1: int, x2: int, y2: int) -> int:
    x = x1 - x2
    y = y1 - y2
    if (x, y) == (0, 0):
        return 0
    elif abs(x) == abs(y):
        return 1
    elif abs(x) + abs(y) <= 3:
        return 1
    elif (x1 + x2 + y1 + y2) % 2 == 0:
        return 2
    elif abs(x) + abs(y) <= 6:
        return 2
    elif abs(x + y) <= 3:
        return 2
    elif abs(x - y) <= 3:
        return 2
    else:
        return 3


def main():
    x1, y1 = map(int, input().split())
    x2, y2 = map(int, input().split())
    print(count_min_operation(x1, y1, x2, y2))


if __name__ == '__main__':
    main()
