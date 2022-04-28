





def main():
    n = int(input())
    A = list(map(int, input().split()))
    A = sorted(A)
    ans = n
    sum = 0
    c = 1
    for i in range(n - 1):
        sum += A[i]
        
        
        if A[i + 1] > sum * 2:
            ans -= c
            c = 1
        
        else:
            c += 1
        
    print(ans)
    
main()