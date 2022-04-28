





def main():
    n, k = map(int, input().split())
    list_s = list(input())
    
    list_a = []
    memo = []
    for i in range(n):
        s = list_s[i]
        if (i == 0):
            memo = [s, 1]
            continue
        
        if (i == n - 1):
            if (memo[0] == s):
                memo[1] += 1
                list_a.append(memo)
                continue
            
            if (memo[0] != s):
                list_a.append(memo)
                list_a.append([s, 1])
                continue
                
        if (memo[0] != s):
            list_a.append(memo)
            memo = [s, 1]
            continue
        
        if (memo[0] == s):
            memo[1] += 1
            continue
    
    len_a = len(list_a)
    count = 0
    for a in list_a:
        if a[0] == '0':
            count += 1
    
    if count <= k:
        print(n)
        exit()
        
    ans = 0
    condidate = 0
    count = 0
    
    for i in range(len_a):
        condidate = 0
        count = 0
        for j in range(i, len_a):
            if (list_a[j][0] == '1'):
                condidate += list_a[j][1]
            
            if count >= k:
                break

            if (list_a[j][0] == '0'):
                condidate += list_a[j][1]
                count += 1
                continue
        
        ans = max(ans, condidate)
    
    print(ans)
    
if __name__ == '__main__':
    main()

            
        