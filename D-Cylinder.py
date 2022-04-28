from collections import deque


def main():
    q = int(input())
    number_list = []
    for _ in range(q):
        query = list(map(int, input().split()))
        if query[0] == 1:
            number_list.append([query[1], query[2]])
        else:
            ans = 0
            c = query[1]
            while(c > 0):
                if number_list[0][1] <= c:
                    ans += number_list[0][0] * number_list[0][1]
                    c -= number_list[0][1]
                    number_list.pop(0)
                else:
                    ans += number_list[0][0] * c
                    number_list[0][1] -= c
                    c = 0
            print(ans)


if __name__ == '__main__':
    main()
