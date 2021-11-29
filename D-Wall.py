





def is_bool(memo):
    search_list = []
    for i in range(10):
        if memo[i] == 0:
            search_list.append(i)
    
    return search_list
        
def search(now, cost, memo, C, condidate_list):
    if now == 1:
        condidate_list.append(cost)
        
    memo[now] = 1
    search_list = is_bool(memo)
    
    for s in search_list:
        
        
        search(s, cost + C[now][s], memo, C, condidate_list)
        memo[s] = 0
        
def main():
    h, w = map(int, input().split())
    C = []
    for i in range(10):
        c = list(map(int, input().split()))
        C.append(c)
    
    A = []
    for i in range(h):
        a = list(map(int, input().split()))
        A.append(a)
        
    distance_list = []
    for i in range(10):
        memo = [0 for _ in range(10)]
        condidate_list = []
        cost = 0
        now = i
        
        search(now, cost, memo, C, condidate_list)
        
        if len(condidate_list) == 0:
            distance_list.append(0)
            continue
        
        distance_list.append(min(condidate_list))
    
    ans = 0
    for i in range(h):
        for j in range(w):
            a = A[i][j]
            if a == -1:
                continue
            
            ans += distance_list[a]
    
    print(ans)
    
if __name__ == '__main__':
    main()
    