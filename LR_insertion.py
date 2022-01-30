def main():
    n = int(input())
    s = input()
    ans_list = [-1 for _ in range(n + 1)]
    index = 0
    left = 0
    right = n
    
    for i in range(n):
        if s[i] == 'L':
            ans_list[right] = i
            right -= 1
        
        if s[i] == 'R':
            ans_list[left] = i
            left += 1
            
    for i in range(n + 1):
        if ans_list[i] == -1:
            ans_list[i] = n
            break
        
            
            
    
    
    print(*ans_list)
    

if __name__ == '__main__':
    main()
