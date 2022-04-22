





def DFS(branch_information, now, branch_seen, branch_color, cost):
    branch_seen[now - 1] = True
    if cost % 2 == 0:
        branch_color[now - 1] = 1
        
    for i in range(len(branch_information)):
        if branch_information[i][0] == now and branch_seen[branch_information[i][1] - 1] == False:
            DFS(branch_information, branch_information[i][1], branch_seen, branch_color, cost + branch_information[i][2])
            
        if branch_information[i][1] == now and branch_seen[branch_information[i][0] - 1] == False:
            DFS(branch_information, branch_information[i][0], branch_seen, branch_color, cost + branch_information[i][2])
            
def main():
    n = int(input())
    branch_information = []
    for i in range(n - 1):
        u, v, w = map(int, input().split())
        branch_information.append([u, v, w])
    
    branch_seen = [False for _ in range(n)]
    branch_color = [0 for _ in range(n)]
    
    DFS(branch_information, 1, branch_seen, branch_color, 0)
    
    
    for i in range(n):
        print(branch_color[i])
        
if __name__ == '__main__':
    main()

    
    
    
    
    
    