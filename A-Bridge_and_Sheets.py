import math
l = 0
w = 0
a_list = []


def count_tarps():
    now = 0
    cnt = 0
    for a in a_list:
        if now < a:
            cnt += (a - now + w - 1) // w

        now = a + w

    print(cnt)


if __name__ == '__main__':
    n, l, w = map(int, input().split())
    a_list = list(map(int, input().split()))
    a_list.append(l)
    count_tarps()
