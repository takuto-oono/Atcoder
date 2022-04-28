def main():
    s = input()
    flag = True
    for i in range(len(s) // 2 + 1):
        j = len(s) - i - 1
        if s[i] != s[j]:
            flag = False
            break
    
    if flag:
        print('Yes')
        exit()
        
    b_cnt = 0
    e_cnt = 0
    
    for i in range(len(s)):
        if s[i] == 'a':
            b_cnt += 1
        else:
            break
    
    for i in range(len(s)):
        index = len(s) - i - 1
        if s[index] == 'a':
            e_cnt += 1
        else:
            break
    
    s = 'a' * max(0, e_cnt - b_cnt) + s
    for i in range(len(s) // 2 + 1):
        j = len(s) - i - 1
        if s[i] != s[j]:
            print('No')
            exit()
    
    print('Yes')
        


if __name__  == '__main__':
    main()
