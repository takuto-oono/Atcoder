





def main():
    q = int(input())
    lr_list = []
    for i in range(q):
        l, r = map(int, input().split())
        lr_list.append([l, r])
    
    prime = [i + 1 for i in range(10 ** 5)]
    
    i = 1
    while(i < len(prime)):
        j = i + 1
        
        while(j < len(prime)):
            x = prime[j]
            if x % prime[i] == 0:
                prime.remove(x)
            
            else:
                j += 1
                
        i += 1
        
    count_dic = {}
    c = 0
    for i in range(len(prime)):
        
        n1 = prime[i]
        
        if n1 == 2:
            continue
        
        n2 = (n1 + 1) // 2
        
        for j in range(i):
            if n2 == prime[j]:
                c += 1
                break
        
        count_dic[i] = c

    
    for i in range(q):
        l = lr_list[i][0]
        r = lr_list[i][1]
        
        
        ans = count_dic[r] - count_dic[l - 1]
        print(ans)
        
    
        
        
        
            

if __name__ == '__main__':
    main()

        
        