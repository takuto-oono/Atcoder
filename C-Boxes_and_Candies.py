





def main():
    n, x = map(int, input().split())
    list_a = list(map(int, input().split()))
    sum_a = sum(list_a)
    
    if (n <= 2):
        ans = max(0, sum_a - x)
        print(ans)
        exit()
    
    for i in range(n - 2):
        a_i = list_a[i]
        a_j = list_a[i + 1]
        a_k = list_a[i + 2]
        
        if (i == n - 3):
            y = max(a_i + a_j, a_k + a_j)
            if y > x:
                list_a[i + 1] -= y - x
                
            continue
        
        if (a_i + a_j > x and a_j + a_k > x):
            if (a_i + a_j - x <= a_j):
                list_a[i + 1] -= (a_i + a_j - x)
                continue
            
            list_a[i + 1] = 0
            list_a[i] -= a_i - x
            continue
        
        if (a_i + a_j <= x and a_j + a_k > x):
            continue
        
        if (a_i + a_j > x and a_j + a_k <= x):
            if (a_i + a_j - x <= a_j):
                list_a[i + 1] -= (a_i + a_j - x)
                continue
            
            list_a[i + 1] = 0
            list_a[i] -= a_i - x
            continue
        
    ans = sum_a - sum(list_a)
    
    
    print(ans)

if __name__ == '__main__':
    main()

        
        
            
        
        