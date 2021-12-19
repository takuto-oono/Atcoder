





def main():
    list_ab = []
    n = int(input())
    ans = 0
    for i in range(n):
        a, b = map(int, input().split())
        ans -= b
        list_ab.append(a + b)
    
    list_ab.sort(reverse=True)
    
    for i in range(n):
        if i % 2 == 1:
            continue
        
        ans += list_ab[i]
    
    print(ans)
    
    
if __name__ == '__main__':
    main()
