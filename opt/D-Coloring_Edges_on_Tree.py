import sys
sys.setrecursionlimit(100000)





def main():
    n = int(input())
    branch = [[] for _ in range(n)]
    
    for i in range(n - 1):
        a, b = map(int, input().split())
        a -= 1
        b -= 1
        branch[a].append([b, i])
    
    branch[a].sort()
    edges_list = [0 for _ in range(n - 1)]
    def create_edge(edges_list, branch, now, used_edge):
        edge = 0
        for i in range(len(branch[now])):
            edge += 1
            if used_edge == edge:
                edge += 1
            
            edges_list[branch[now][i][1]] = edge
            create_edge(edges_list, branch, branch[now][i][0], edge)
    
    create_edge(edges_list, branch, 0, 0)
    
    print(max(edges_list))
    for edge in edges_list:
        print(edge)
            
if __name__ == '__main__':
    main()

            
        