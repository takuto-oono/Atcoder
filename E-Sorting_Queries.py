import heapq

def process(x: int) -> None:
    l.append(l)
    

def main():
    q = int(input())
    h = []
    l = []
    heapq.heapify(h)
    for _ in range(q):
        query = list(map(int, input().split()))
        if query[0] == 1:
            process1(query[1])
        if query[0] == 2:
            process2()
        if query[0] == 3:
            process3()


if __name__ == '__main__':
    main()
