





def main():
    x = input()
    t = 'T'
    s = 'S'
    n = len(x)
    memo = [1 for _ in range(n)]
    last_index = 0
    
    for i in range(n):
        if i == 0:
            last_index = 0
            continue
        
        if last_index == -1:
            last_index = i
            continue
        
        c = x[i]
        if c == s:
            last_index = i
            continue
        
        if c == t:
            if x[last_index] == t:
                last_index = i
                continue
            
            if x[last_index] == s:
                memo[i] = 0
                memo[last_index] = 0
                
                y = 0
                count = 0
                for j in range(last_index):
                    y = last_index - j - 1
                    if memo[y] == 1:
                        break
                    
                    count += 1
                    
                if count < last_index:
                    last_index = y
                    continue
                
                if count == last_index:
                    last_index = -1
                    
    ans = 0
    for i in range(n):
        if memo[i]:
            ans += 1
    
    print(ans)
    
if __name__ == '__main__':
    main()