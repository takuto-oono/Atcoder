





def main():
    n = int(input())
    a_list = list(map(int, input().split()))
    s_list = [0]
    s = 0
    
    for i in range(n):
        s += a_list[i]
        s_list.append(s)
    
    s_list.sort()
    
    ans = 0
    i = 0
    while(i < n):
        j = i + 1
        
        while(j < n + 1):
            
            if s_list[i] != s_list[j]:
                break
            
            j += 1
        
        
        
        ans += (j - i) * (j - i - 1) // 2
        i = j
    
    print(ans)
    
if __name__ == '__main__':
    main()
        
        
    
    