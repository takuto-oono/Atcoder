





def main():
    n = int(input())
    list_f = []
    for i in range(n):
        f = list(map(int, input().split()))
        list_f.append(f)
        
    list_p = []
    for i in range(n):
        p = list(map(int, input().split()))
        list_p.append(p)
        
    ans = -10 ** 10
    for i in range(2 ** 10):
        management_time = []
        for j in range(10):
            if ((i >> j) & 1):
                management_time.append(j)
        
        if (len(management_time) == 0):
            continue
        
        benefit = 0
        for j in range(n):
            c = 0
            for k in range(10):
                if k in management_time:
                    if list_f[j][k]:
                        c += 1
            
            benefit += list_p[j][c]
            
        
        ans = max(benefit, ans)
    
    print(ans)
    
if __name__ == '__main__':
    main()

        