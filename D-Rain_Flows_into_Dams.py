





def main():
    n = int(input())
    A = list(map(int, input().split()))
    M = [-1] * n
    m = 0
    for i in range(n):
        if i % 2 == 0:
            m += A[i]
        else:
            m -= A[i]
            
    M[0] = m
    for i in range(1, n):
        M[i] = 2 * A[i - 1] - M[i - 1]
    
    print(*M)
    
if __name__ == "__main__":
    main()
    
