





def main():
    n, q = map(int, input().split())
    tree = [[] for _ in range(n)]
    
    for i in range(n - 1):
        a, b = map(int, input().split())
        tree[a - 1].append(b - 1)
        tree[b - 1].append(a - 1)
        
    add_list = [0 for _ in range(n)]
    for i in range(q):
        p, x = map(int, input().split())
        add_list[p - 1] += x
    
    ans = [0 for _ in range(n)]
    bool_list = [True for _ in range(n)]
    bool_list[0] = False
    ans[0] = add_list[0]
    sum = ans[0]
    
    def dfs(x, bool_list, sum):
        for y in tree[x]:
            if bool_list[y]:
                sum += add_list[y]
                ans[y] = sum
                bool_list[y] = False
                for z in tree[y]:
                    if bool_list[z]:    
                        dfs(y, bool_list, sum)
                        break
                    
                sum -= add_list[y]
    
    dfs(0, bool_list, sum)
    print(*ans)
    
    
main()

        
        