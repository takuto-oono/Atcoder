

def main():
    n = int(input())
    t_list = []
    skill_branch = [[] for _ in range(n - 1)]
    for i in range(n):
        l = list(map(int, input().split()))
        t = l.pop(0)
        t_list.append(t)
        r = l.pop(0)
        
        for j in range(r):
            skill_branch[l[j] - 1].append(i)
    
    def search(now, goal, todo_list):
        
    
            

    

if __name__ == '__main__':
    main()
