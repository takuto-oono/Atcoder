





def Ruler(A, i, n, k):
    s = 0
    for j in range(i, n):
        s += A[j]
        if s >= k:
            return n - j
    
    return 0

def main():
    n, k = map(int, input().split())
    A = list(map(int, input().split()))
    ans = 0
    for i in range(n):
        ans += Ruler(A, i, n, k)
    
    print(ans)

main()



