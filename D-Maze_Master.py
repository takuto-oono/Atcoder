





def create_adjacent_list(S, h, w):
    Adjacent = [[[] for _ in range(w)] for _ in range(h)]
    for i in range(h):
        for j in range(w):
            if S[i][j] == '#':
                continue
            
            if i != h - 1:
                if S[i + 1][j] == '.':
                    Adjacent[i][j].append([i + 1, j])
                
            if j != w - 1:
                if S[i][j + 1] == '.':
                    Adjacent[i][j].append([i, j + 1])
            
            if i != 0:
                if S[i - 1][j] == '.':
                    Adjacent[i][j].append([i - 1, j])
            
            if j != 0:
                if S[i][j - 1] == '.':
                    Adjacent[i][j].append([i, j - 1])
    
    return Adjacent

def all_search(start_x, start_y, goal_x, goal_y, c, Adjacent, memo):
    if [goal_x, goal_y] in Adjacent[start_x][start_y]:
        return c + 1
    
    
    
    for nex in Adjacent[start_x][start_y]:
        if nex not in memo:
            memo.append([start_x, start_y])
            all_search(nex[0], nex[1], goal_x, goal_y, c + 1, Adjacent, memo)
    
    
    
def main():
    h, w = map(int, input().split())
    S = []
    for i in range(h):
        s = list(input())
        S.append(s)
        
    Adjacent = create_adjacent_list(S, h, w)
    for i in range(h):
        for j in range(w):
            print(Adjacent[i][j])
            
    ans = 0
    
    for i in range(h):
        for j in range(w):
            for k in range(h):
                for m in range(w):
                    if i == k and j == m:
                        continue
                    
                    ans = max(ans, all_search(i, j, k, m, 0, Adjacent, []))
                    print(all_search(i, j, k, m, 0, Adjacent, []))
        
    
if __name__ == '__main__':
    main()
        
        
        
    
    