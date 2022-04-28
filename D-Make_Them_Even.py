a_list = []
h = 0
w = 0
operation_list = []


def operate() -> None:
    for y in range(h):
        is_had = False
        for x in range(w):
            a = a_list[y][x]
            if is_had:
                operation_list.append([y + 1, x, y + 1, x + 1])
                if a % 2 == 1:
                    is_had = False

                a_list[y][x - 1] -= 1
                a_list[y][x] += 1

                continue

            else:
                if a % 2 == 0:
                    continue

                is_had = True

    x = w - 1
    is_had = False
    for y in range(h):
        a = a_list[y][x]
        if is_had:
            operation_list.append([y, x + 1, y + 1, x + 1])
            if a % 2 == 1:
                is_had = False

            a_list[y - 1][x] -= 1
            a_list[y][x] += 1

            continue

        else:
            if a % 2 == 0:
                continue

            is_had = True


def print_operation_list() -> None:
    n = len(operation_list)
    print(n)
    for operation in operation_list:
        print(*operation)


if __name__ == '__main__':
    h, w = map(int, input().split())
    operation_list = []
    for _ in range(h):
        a = list(map(int, input().split()))
        a_list.append(a)

    operate()

    print_operation_list()
