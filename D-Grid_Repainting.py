





def main():
    h, w = map(int, input().split())
    S = []
    for i in range(h):
        s = list(input())
        S.append(s)
        
    path = [[[] for _ in range(w)] for _ in range(h)]
    count = 0
    for i in range(h):
        for j in range(w):
            if S[i][j] == '#':
                count += 1
                continue
            
            if i == 0 and j == 0:
                if S[i][j + 1] == '.':
                    path[i][j].append([i, j + 1])
                
                if S[i + 1][j] == '.':
                    path[i][j].append([i + 1, j])
                
                continue
                
            if i == h - 1 and j == w - 1:
                continue
            
            if j != w - 1:
                if S[i][j + 1] == '.':
                    path[i][j].append([i, j + 1])
                    
            if i != h - 1:
                if S[i + 1][j] == '.':
                    path[i][j].append([i + 1, j])
                    
            if i != 0:
                if S[i - 1][j] == '.':
                    path[i][j].append([i - 1, j])
                    
            if j != 0:
                if S[i][j - 1] == '.':
                    path[i][j].append([i, j - 1])
                    
    def BFS(path):
        dist = [[-1 for _ in range(w)] for _ in range(h)]
        dist[0][0] = 0
        todo = [[0,0]]
        
        while(len(todo) > 0):
            now = todo[0]
            todo.remove(now)
            
            for p in path[now[0]][now[1]]:
                next_h = p[0]
                next_w = p[1]
                
                if dist[next_h][next_w] != -1:
                    continue
                
                dist[next_h][next_w] = dist[now[0]][now[1]] + 1
                todo.append(p)
                
        return dist[h - 1][w - 1]
    
    if BFS(path) == -1:
        print(-1)
        exit()
        
    ans = h * w - BFS(path) - count - 1
    print(ans)

if __name__ == '__main__':
    main()
