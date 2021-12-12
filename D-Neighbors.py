





def main():
    n, m = map(int, input().split())
    ab_list = []
    ab_dic = {}
    for i in range(m):
        a, b = map(int, input().split())
        ab_list.append([a, b])
        
    
    ab_count = [0 for _ in range(n)]
    
    for i in range(m):
        a = ab_list[i][0]
        b = ab_list[i][1]
        ab_count[a - 1] += 1
        ab_count[b - 1] += 1
    
    for i in range(n):
        if ab_count[i] >= 3:
            print('No')
            exit()
    
    memo = [0 for i in range(n)]
    branch_list = []
    for i in range(m):
        a = ab_list[i][0]
        b = ab_list[i][1]
        
        for j in range(len(branch_list)):
            branch = branch_list[j]
            if (branch[0] == a and branch[1] == b) or (branch[1] == a and branch[0] == b):
                print('No')
                exit()
            
            if branch[0] == a:
                branch[0] = b
                continue
            
            if branch[0] == b:
                branch[0] = a
                continue
            
            if branch[1] == a:
                branch[1] = b
                continue
            
            if branch[1] == b:
                branch[1] = a
                continue
            
            
            
        
            
            
            
        
        
        
        
    
    

if __name__ == '__main__':
    main()
        
        
    