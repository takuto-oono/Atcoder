





def main():
    n = int(input())
    testimonies = []
    for i in range(n):
        a = int(input())
        testimony = []
        for j in range(a):
            x, y = map(int, input().split())
            testimony.append([x, y])
        
        testimonies.append(testimony)
    
    ans = 0
    for i in range(2 ** n):
        honest_list = []
        for j in range(n):
            if ((i >> j) & 1):
                honest_list.append(j + 1)
        
        condidate = len(honest_list)
        
        for j in range(n):
            if j + 1 not in honest_list:
                continue
            
            for k in range(len(testimonies[j])):
                x = testimonies[j][k][0]
                y = testimonies[j][k][1]
                if y == 1 and x in honest_list:
                    continue
                
                if y == 0 and x not in honest_list:
                    continue
                    
                condidate = 0
        
        ans = max(ans, condidate)
    
    print(ans)
    
if __name__ == '__main__':
    main()