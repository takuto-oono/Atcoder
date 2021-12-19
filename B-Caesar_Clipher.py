





def change(s, x):
    s_int = ord(s)
    t_int = s_int + x
    if t_int >= 123:
        t_int = 97 + t_int - 123
    
    return chr(t_int)

def main():
    string_s = input()
    string_t = input()
    t = string_t[0]
    s = string_s[0]
    if len(string_t) == 1:
        print('Yes')
        exit()
        
    x = ord(t) - ord(s)
    if x < 0:
        x += 26
    
    for i in range(len(string_s)):
        if change(string_s[i], x) != string_t[i]:
            print('No')
            exit()
    
    print('Yes')
    
        
    
    
    
        
if __name__ == '__main__':
    main()
    
