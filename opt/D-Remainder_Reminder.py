





def main():
    n, k = map(int, input().split())
    if (k == 0):
        print(n ** 2)
        exit()
        
    ans = 0
    
    
    for b in range(k + 1, n + 1):
        m = k
        x = (n - k) // b
        ans += (x + 1) * (b - k)
        y = x * b + k
        z = y + b - k - 1
        
        if (z > n):
            
            ans -= (z - n)
            
        '''while(True):
            if (y + b - k - 1 <= n):
                break
            
            ans -= 1
            y -= 1'''
    
    print(ans)
    
if __name__ == '__main__':
    main()
