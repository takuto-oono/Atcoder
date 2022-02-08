import math


def cal_number_of_stamps(x, y):
    ans = math.ceil((y - x) / 10)
    if ans < 0:
        ans = 0

    return ans


if __name__ == '__main__':
    x, y = map(int, input().split())
    print(cal_number_of_stamps(x, y))
