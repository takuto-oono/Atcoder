





def main():
    h, w = map(int, input().split())
    s_list = []
    for i in range(h):
        s = list(input())
        s_list.append(s)
        
    count_h = [[0 for _ in range(w)] for _ in range(h)]
    c = 0
    for i in range(h):
        c = 0
        for j in range(w):
            if s_list[i][j] == '#':
                c = 0
                continue
            
            c += 1
            count_h[i][j] = c
            
        memo = 0
        for j in reversed(range(w)):
            if count_h[i][j] == 0:
                memo = 0
                continue
            
            if memo == 0:
                memo = count_h[i][j]
            
            count_h[i][j] = memo
    
    count_w = [[0 for _ in range(w)] for _ in range(h)]
    c = 0
    for i in range(w):
        c = 0
        for j in range(h):
            if s_list[j][i] == '#':
                c = 0
                continue
            
            c += 1
            count_w[j][i] = c
            
        memo = 0
        for j in reversed(range(h)):
            if count_h[j][i] == 0:
                memo = 0
                continue
            
            if memo == 0:
                memo = count_w[j][i]
            
            count_w[j][i] = memo
            
    ans = 0
    for i in range(h):
        for j in range(w):
            ans = max(ans, count_h[i][j] + count_w[i][j] - 1)
    
    print(ans)
    
if __name__ == '__main__':
    main()

