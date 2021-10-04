





def main():
    n, k = map(int, input().split())
    A = list(map(int, input().split()))
    ans = 0
    sum = 0
    j = 0
    for i in range(n):

        while(sum < k):
            if j == n:
                break
            sum += A[j]

            if sum >= k:
                j += 1
                break

            j += 1

        if (sum < k):
            break

        ans += n - j + 1
        sum -= A[i]

    print(ans)

        


main()






