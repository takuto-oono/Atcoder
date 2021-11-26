





def is_empty_list(L, w):
    return sum(L) == -1 * w
    
def main():
    h, w, k = map(int, input().split())
    S = []
    for i in range(h):
        s = list(input())
        S.append(s)
        
    Ans = [[-1 for _ in range(w)] for _ in range(h)]
    
    c = 1
    for i in range(h):
        for j in range(w):
            if S[i][j] == '#':
                Ans[i][j] = c
                c += 1
    
    c = 0
    for i in range(h):
        if is_empty_list(Ans[i], w):
            print(i)
            continue
        
        c += 1
        for j in range(w):
            if Ans[i][j] == c + 1:
                c += 1
                
            
            Ans[i][j] = c
        
    for i in range(h):
        if is_empty_list(Ans[i], w):
            if i == h - 1:
                for j in reversed(range(i)):
                    if is_empty_list(Ans[j], w) == False:
                        Ans[i] = Ans[j]
                        break
            
            else:
                for j in range(i + 1, h):
                    if is_empty_list(Ans[j], w) == False:
                        Ans[i] = Ans[j]
                        break
                    
    for i in range(h):
        print(*Ans[i])  

if __name__ == '__main__':
    main()
