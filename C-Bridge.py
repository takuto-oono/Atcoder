





def BFS(branch_list, m, n):
    visit_list = [False for _ in range(n)]
    visit_list[0] = True
    todo_list = [1]
    
    while(len(todo_list) > 0):
        visit = todo_list[0]
        todo_list.remove(visit)
        for i in range(m):
            a = branch_list[i][0]
            b = branch_list[i][1]
            if a == visit:
                if visit_list[b - 1]:
                    continue
                
                visit_list[b - 1] = True
                todo_list.append(b)
                continue
            
            if b == visit:
                if visit_list[a - 1]:
                    continue
                
                visit_list[a - 1] = True
                todo_list.append(a)
                continue
    
    for i in range(n):
        if visit_list[i] == False:
            return True
    
    return False
        
def main():
    n, m = map(int, input().split())
    ab_list = []
    for i in range(m):
        a, b = map(int, input().split())
        ab_list.append([a, b])
    
    ans = 0
    for i in range(m):
        branch_list = [ab_list[j] for j in range(m) if i != j]
        
        if BFS(branch_list, m - 1, n):
            ans += 1
    
    print(ans)
    
if __name__ == '__main__':
    main()

        