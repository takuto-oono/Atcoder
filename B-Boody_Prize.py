





def main():
    n = int(input())
    A = list(map(int, input().split()))

    for i in range(n):
        A[i] = [A[i], i]

    A.sort()
    ans = 1 + A[-2][1]
    print(ans)

main()
