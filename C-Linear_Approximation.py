





def main():
    n = int(input())
    list_a = list(map(int, input().split()))
    
    for i in range(n):
        list_a[i] -= i + 1

    list_a.sort()
    
    if n % 2 == 1:
        b = list_a[n // 2]
    
    else:
        b = (list_a[n // 2] + list_a[n // 2 - 1]) // 2
    
    ans = 0
    for a in list_a:
        ans += abs(a - b)
    
    print(ans)
    
if __name__ == '__main__':
    main()
