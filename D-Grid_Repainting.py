





def main():
    h, w = map(int, input().split())
    S = []
    for i in range(h):
        s = list(input())
        S.append(s)
        
    path = [[[] for _ in range(w)] for _ in range(h)]
    print(path)
    
    for i in range(h):
        for j in range(w):
            if S[i][j] == '#':
                continue
            
            if i == 0 and j == 0:
                if S[i][j + 1] == '.':
                    path[i][j].append([i, j + 1])
                
                if S[i + 1][j] == '.':
                    path[i][j].append([i + 1, j])
                
                continue
                
            if i == h - 1 and j == w - 1:
                path[i][j] = 1
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
                    
    for i in range(h):
        print(path[i])

    condidate_path = []
    condidate_path_list = []
    
    def search(i, j, path, condidate_path, condidate_path_list, h, w):
        print(i, j)
        condidate_path.append([i, j])
        if i == h - 1 and j == w - 1:
            condidate_path_list.append(condidate_path)
            
            
        
        elif i == 0 and j == 0:
            if path[i][j] != []:
                
                for k in range(len(path[i][j])):
                    p = path[i][j][k]
                    print(i, j, p)
        
                    search(p[0], p[1], path, condidate_path, condidate_path_list, h, w)
                
                    condidate_path.remove([p[0], p[1]])
        
        else:
            if path[i][j] != []:
                for k in range(len(path[i][j])):
                    
                    p = path[i][j][k]
                    print(i, j, p)
                    
                    if p == condidate_path[-1]:
                        continue
                    
                    search(p[0], p[1], path, condidate_path, condidate_path_list, h, w)
                    condidate_path.remove([p[0], p[1]])
    
    search(0, 0, path, condidate_path, condidate_path_list, h, w)
    
    for condidate in condidate_path_list:
        print(condidate)
                
                
        
if __name__ == '__main__':
    main()

        
        

            
            
            
                