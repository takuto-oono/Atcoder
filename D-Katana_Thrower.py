





def main():
    n, h = map(int, input().split())
    A = []
    B = []
    for i in range(n):
        a, b = map(int, input().split())
        A.append(a)
        B.append(b)
    
    B.sort(reverse=True)
    ans = 0
    a_max = max(A)
    
    for i in range(n):
        if h > 0 and B[i] > a_max:
            ans += 1
            h -= B[i]
            
        if h <= 0:
            print(ans)
            exit()
            
    ans += h // a_max + 1
    if h % a_max == 0:
        ans -= 1
    
    print(ans)
    
if __name__ == '__main__':
    main()
