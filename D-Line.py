import networkx as nx





def create_graph(n, x, y):
    graph = nx.Graph()
    nx.add_path(graph, [i for i in range(1, n + 1)])
    nx.add_path(graph, [x, y])

    return graph

def insearch_distance(graph, n):
    ans = [0 for i in range(n - 1)]
    for i in range(1, n):
        for j in range(i + 1, n + 1):
            if (nx.has_path(graph, source=i, target=j)):
                distance = len(nx.shortest_path(graph, source=i, target=j)) - 1
                ans[distance - 1] += 1
    
    return ans

def print_ans(ans):
    for a in ans:
        print(a)
                


def main():
    n, x, y = map(int, input().split())
    graph = create_graph(n, x, y)
    ans = insearch_distance(graph, n)
    print_ans(ans)
    

if __name__ == '__main__':
    main()


