





def main():
    S = list(input())
    ans = 0
    i = 0
    j = len(S) - 1
    if len(S) == 1:
        print(0)
        exit()
    
    while(i < j):
        front = S[i]
        end = S[j]
        
        if front != 'x' and end != 'x' and front != end:
            print(-1)
            exit()
            
        if front == end:
            i += 1
            j -= 1
            continue
        
        if front == 'x' and end != 'x':
            ans += 1
            i += 1
            continue
        
        if front != 'x' and end == 'x':
            ans += 1
            j -= 1
            
    print(ans)
    
if __name__ == '__main__':
    main()

