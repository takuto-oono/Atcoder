





def BFS(i, j, A, todo):
    if A[i][j] == '#':
        return 
    
def main():
    h, w = map(int, input().split())
    A = []
    for i in range(h):
        a = list(input())
        A.append(a)
        
    for i in range(h):
        for j in range(w):
            if A[i][j] == '.':
                A[i][j] = -1
                
