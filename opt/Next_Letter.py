





def diffrence_a(s):
    return 123 - ord(s)

def change(s, x):
    x %= 26
    
    if ord(s) + x > 122:
        return chr(ord(s) + x  - 122 + 96)
    
    return chr(ord(s) + x)

def main():
    s_list = list(input())
    k = int(input())
    
    for i in range(len(s_list)):
        if k <= 0:
            break

        s = s_list[i]
        if i == len(s_list) - 1 and k > 0:
            s_list[i] = change(s, k)
            continue
        
        if diffrence_a(s) <= k and s != 'a':
            s_list[i] = 'a'
            k -= diffrence_a(s)
            continue
        
        if diffrence_a(s) > k:
            continue
    
    print(''.join(s_list))
    
if __name__ == '__main__':
    main()