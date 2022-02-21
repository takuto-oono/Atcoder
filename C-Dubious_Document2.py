if __name__ == '__main__':
    s = input()
    t = input()
    
    
    for i in reversed(range(0, len(s) - len(t) + 1)):
        
        x = s[i: i + len(t)]
        j = 0
        flag = True
        while(j < len(t)):
            if x[j] != '?' and x[j] != t[j]:
                flag = False
                break
            j += 1
            
        if flag:
            s = s[:i] + t + s[i + 1 + j:]
            ans = ''
            for i in range(len(s)):
                if s[i] == '?':
                    ans += 'a'
                else:
                    ans += s[i]
                    
            print(ans)
            exit()
            
    print('UNRESTORABLE')
            
            
