





def main():
    n = int(input())
    Graph = [[] for _ in range(n)]
    for i in range(n - 1):
        a, b, c = map(int, input().split())
        a -= 1
        b -= 1
        Graph[a].append([b, c])
        Graph[b].append([a, c])
    
    q, k = map(int, input().split())
    k -= 1
    query_list = []
    for i in range(q):
        x, y = map(int, input().split())
        query_list.append([x - 1, y - 1])
    
    def BFS(Graph, k):
        distance_list = [10 ** 10 for _ in range(n)]
        distance_list[k] = 0
        todo_list = [k]
        
        while(len(todo_list) > 0):
            f = todo_list.pop(0)
            
            for branch in Graph[f]:
                t = branch[0]
                dis = branch[1]
                if distance_list[t] != 10 ** 10:
                    continue
                
                todo_list.append(t)
                distance_list[t] = distance_list[f] + dis
                
        return distance_list
                
    distance_list = BFS(Graph, k)
    
    for i in range(q):
        x = query_list[i][0]
        y = query_list[i][1]
        ans = distance_list[x] + distance_list[y]
        print(ans)
        
if __name__ == '__main__':
    main()

        
        