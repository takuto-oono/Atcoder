import math


def create_length_squared_list(xy_coordinates):
    length_squared_list = []
    for i in range(len(xy_coordinates) - 1):
        xi = xy_coordinates[i][0]
        yi = xy_coordinates[i][1]
        for j in range(i + 1, len(xy_coordinates)):
            xj = xy_coordinates[j][0]
            yj = xy_coordinates[j][1]
            length_squared_list.append((xi - xj) ** 2 + (yi - yj) ** 2)

    return length_squared_list


def find_ans(length_squared_list):
    ans_squared = max(length_squared_list)
    ans = math.sqrt(ans_squared)
    return ans


if __name__ == '__main__':
    n = int(input())
    xy_coordinates = []
    for i in range(n):
        x, y = map(int, input().split())
        xy_coordinates.append([x, y])

    print(find_ans(create_length_squared_list(xy_coordinates)))
