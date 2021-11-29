





def main():
    n = int(input())
    S = list(input())
    
    begin = []
    end = []
    c = 0
    for i in range(n):
        s = S[i]
        if s == ')':
            c += 1
            if c > 0:
                begin.append('(')
                c -= 1
        
        else:
            c -= 1
        
    if c < 0:
        end = [')'] * (-c)
        
    ans = ''.join(begin) + ''.join(S) + ''.join(end)
    print(ans)
    
if __name__ == '__main__':
    main()
