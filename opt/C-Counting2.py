





def main():
    n, q = map(int, input().split())
    a_list = list(map(int, input().split()))
    x_list = []
    for i in range(q):
        x = int(input())
        x_list.append([x, i])
        
    
    x_list.sort()
    a_list.sort()
    
    j = 0
    count = 0
    for i in range(q):
        x = x_list[i][0]
        
        
        while(j < n):
            if a_list[j] < x:
                j += 1
                count += 1
                continue
            
            
            break
        
        x_list[i].append(count)
        
        

    
    x_list = sorted(x_list, key=lambda x: x[1])
    for i in range(q):
        print(n - x_list[i][2])

if __name__ == '__main__':
    main()
    