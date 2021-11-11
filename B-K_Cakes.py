





def main():
    k, t = map(int, input().split())
    A = list(map(int, input().split()))
    A.sort(reverse=True)
    
    for i in range(t - 1):
        x = A[i]
        y = A[i + 1]
        m = min(x, y)
        A[i], A[i + 1] = min(x - m, y - m), max(x - m, y - m)
    
    ans = max(A[t - 1] - 1, 0)
    print(ans)
    
if __name__ == '__main__':
    main()

        