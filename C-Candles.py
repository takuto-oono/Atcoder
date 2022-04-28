





def main():
    n, k = map(int, input().split())
    x_list = list(map(int, input().split()))
    
    x_plus_list = []
    x_minus_list = []
    ans = 10 ** 12
    
    for x in x_list:
        if x <= 0:
            x_minus_list.append(abs(x))
        
        if x >= 0:
            x_plus_list.append(x)
        
    x_minus_list.sort()
    
    
    x_plus_len = len(x_plus_list)
    x_minus_len = len(x_minus_list)
    
    if x_list == [0]:
        print(0)
        exit()
    
    if 0 not in x_list:
    
        for i in range(x_minus_len + 1):
            if k - i >= x_plus_len or k - i < 0:
                continue
        
            if i == 0:
                if x_plus_len >= k:
                    distance = x_plus_list[k - 1]
            
                else:
                    distance = 10 ** 12
            
            else:
                distance = 2 * x_minus_list[i - 1] + x_plus_list[k - i - 1]
            
            ans = min(ans, distance)
    
        for i in range(x_plus_len + 1):
            if k - i >= x_minus_len or k - i < 0:
                continue
        
            if i == 0:
                if x_minus_len >= k:
                    distance = x_minus_list[k - 1]
            
                else:
                    distance = 10 ** 12
        
            distance = 2 * x_plus_list[i - 1] + x_minus_list[k - i - 1]
            ans = min(ans, distance)
            
    else:
        for i in range(x_minus_len + 1):
            if k - i + 1 >= x_plus_len or k - i < 0:
                continue
        
            if i == 0:
                if x_plus_len >= k:
                    distance = x_plus_list[k - 1]
            
                else:
                    distance = 10 ** 12
            
            else:
                distance = 2 * x_minus_list[i - 1] + x_plus_list[k - i - 1 + 1]
            
            ans = min(ans, distance)
    
        for i in range(x_plus_len + 1):
            if k - i + 1 >= x_minus_len or k - i < 0:
                continue
        
            if i == 0:
                if x_minus_len >= k:
                    distance = x_minus_list[k - 1]
            
                else:
                    distance = 10 ** 12
        
            distance = 2 * x_plus_list[i - 1] + x_minus_list[k - i - 1 + 1]
            ans = min(ans, distance)
        
        
    print(ans)
    
main()

    
        
    
    
            
        