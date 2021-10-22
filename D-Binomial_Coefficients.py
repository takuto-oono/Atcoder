






def main():
    n = int(input())
    A = list(map(int ,input().split()))
    A.sort()
    
    ans = [A[n - 1]]
    memo = 10 ** 10
    if n == 2:
        print(A[1], A[0])
        exit()

    for i in range(n - 1):
        A[i] *= 2

    for i in range(n - 2):
        if abs(A[i] - A[n - 1]) > abs(A[i + 1] - A[n - 1]):
            continue

        ans.append(A[i] // 2)
        break

    print(*ans)

if __name__ == '__main__':
    main()

