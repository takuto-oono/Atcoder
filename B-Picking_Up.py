





from math import dist


def main():
    n = int(input())
    xy_list = []
    for i in range(n):
        x, y = map(int, input().split())
        xy_list.append([x, y])
    
    distance_list = []
    if n == 1:
        print(1)
        exit()
    
    for i in range(n):
        for j in range(n):
            if i == j:
                continue
            
            p = xy_list[i][0] - xy_list[j][0]
            q = xy_list[i][1] - xy_list[j][1]
            distance_list.append([p, q])
    
    distance_list.sort()
    
    memo = 1
    nocost = 1
    
    for i in range(len(distance_list) - 1):
        if distance_list[i] == distance_list[i + 1]:
            memo += 1
            
            if i == len(distance_list) - 2:
                nocost = max(nocost, memo)
                
            continue
        nocost = max(memo, nocost)
        memo = 1
        
    ans = n - nocost
    print(ans)
    
if __name__ == '__main__':
    main()
    
            