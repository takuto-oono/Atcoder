def base_conversion(n: int) -> None:
    i = 0
    ans = []
    
    while():
        x = 2 ** (i + 1)
        if abs(n) % x == 1:
            ans.append('1')
            
        else:
            ans.append('0')
        
        print(n)
        i += 1
    ans.reverse()
    print(n)
    print("".join(ans))
    
if __name__ == '__main__':
    n = int(input())
    # print(abs(-9 % -8))
    base_conversion(n)
    