def judge(x1, y1, x2, y2, x3, y3):
    area2 = (x2 - x1) * (y3 - y1) - (x3 - x1) * (y2 - y1)
    if area2 == 0:
        return False

    return True


def main():
    n = int(input())
    coordinate_list = []
    for i in range(n):
        x, y = map(int, input().split())
        coordinate_list.append([x, y])

    ans = 0
    for i in range(n - 2):
        xi = coordinate_list[i][0]
        yi = coordinate_list[i][1]
        for j in range(i + 1, n - 1):
            xj = coordinate_list[j][0]
            yj = coordinate_list[j][1]
            for k in range(j + 1, n):
                xk = coordinate_list[k][0]
                yk = coordinate_list[k][1]
                if judge(xi, yi, xj, yj, xk, yk):
                    ans += 1

    print(ans)


if __name__ == '__main__':
    main()
