
def main():
    n = int(input())
    C = list(map(int, input().split()))
    C.sort()
    ans = 1
    memo = 0
    m = 10 ** 9 + 7
    for i in range(n):
        ans *= (C[i] - memo)
        ans %= m
        memo += 1

    ans %= m
    print(ans)

main()





