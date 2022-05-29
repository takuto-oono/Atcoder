import heapq


def main():
    q = int(input())
    li = []
    heapq.heapify(li)
    for _ in range(q):
        query = list(map(int, input().split()))
        if query[0] == 1:
            heapq.heappush(li, query[1])

        if query[0] == 2:
            x = query[1]
            c = query[2]
            b = []
            heapq.heapify(b)
            while(c > 0):
                y = heapq.heapify(li)
                if y == x:
                    c -= 1
                else:
                    heapq.heappush(b, y)
            while(len(li) > 0):
                y = heapq.heappop(li)
                heapq.heappush(b, y)
            li = b

        if query[0] == 3:
            mi = heapq.heappop(li)
            heapq.heappush(li, mi)
            a = [li[i] * -1 for i in range(len(li))]

            heapq.heapify(a)
            ma = heapq.heappop(a) * (-1)
            print(ma - mi)


if __name__ == '__main__':
    main()
