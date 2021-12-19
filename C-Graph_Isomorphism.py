import itertools





def main():
    n, m = map(int, input().split())
    list_ab = []
    list_cd = []
    
    for i in range(m):
        a, b = map(int, input().split())
        list_ab.append([a, b])
    
    for i in range(m):
        c, d = map(int, input().split())
        list_cd.append([c, d])
        
    if m == 0:
        print('Yes')
        exit()
        
    list_p = list(itertools.permutations(range(n), n))
    
    for p in list_p:
        count  = 0
        p = list(p)
        for k in range(m):
            i = list_ab[k][0] - 1
            j = list_ab[k][1] - 1
            if [p[i] + 1, p[j] + 1] in list_cd or [p[j] + 1, p[i] + 1] in list_cd:
                count += 1
        
        if count == m:
            print('Yes')
            exit()
            
    print('No')
    
    
if __name__ == '__main__':
    main()

    
    
    