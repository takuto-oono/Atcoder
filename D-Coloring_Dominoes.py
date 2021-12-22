





from itertools import count


def mod(x):
    m = 1000000007
    return x % m

def main():
    n = int(input())
    s1 = input()
    s2 = input()
    
    before = 0
    
    state = []
    i = 0
    while(i < n):
        if i != n - 1:
            if s1[i] == s1[i + 1]:
                state.append(2)
                i += 2
                continue
            
        state.append(1)
        i += 1
    
    ans = 1
    
    for i in range(len(state)):
        now = state[i]
        if before == 0:
            if now == 2:
                ans *= 6
            
            if now == 1:
                ans *= 3
                
            before = now
            ans = mod(ans)
            continue
        
        if before == 1:
            if now == 2:
                ans *= 2
            
            if now == 1:
                ans *= 2
            
            before = now
            ans = mod(ans)
            continue
        
        if before == 2:
            if now == 2:
                ans *= 3
                ans = mod(ans)
            
            before = now
            continue
    
    print(ans)
    
if __name__ == '__main__':
    main()

                
                
            