import math
import sys


def cal_distance_to_light(coordinates, a_list, index):
    dis = sys.maxsize
    for i in a_list:
        if i == index + 1:
            continue
        dis = min(dis, (coordinates[i - 1][0] - coordinates[index][0]) ** 2 + (coordinates[i - 1][1] - coordinates[index][1]) ** 2)
    return dis


def create_list_distance_to_light(a_list, coordinates):
    distances = [0 for _ in range(len(coordinates))]
    for i in range(len(coordinates)):
        if i + 1 in a_list:
            continue
        distances[i] = cal_distance_to_light(coordinates, a_list, i)
    return distances


def find_ans(distances):
    return math.sqrt(max(distances))


def main():
    n, k = map(int, input().split())
    a_list = list(map(int, input().split()))
    coordinates = []
    for _ in range(n):
        x, y = map(int, input().split())
        coordinates.append([x, y])
    print(find_ans(create_list_distance_to_light(a_list, coordinates)))


if __name__ == '__main__':
    main()
