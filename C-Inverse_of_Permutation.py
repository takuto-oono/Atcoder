





def main():
    n = int(input())
    P = list(map(int, input().split()))
    Q = [0 for i in range(n)]
    for i in range(n):
        p = P[i] - 1
        Q[p] = i + 1

    print(*Q)

main()
