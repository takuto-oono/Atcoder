





def main():
    n = int(input())
    robot_range_list = []
    for i in range(n):
        x, l = map(int, input().split())
        robot_range_list.append([x - l, x + l])
    
    robot_range_list.sort()
    now_max = -10 ** 12
    ans = n
    for i in range(n):
        begin = robot_range_list[i][0]
        end = robot_range_list[i][1]
        if now_max > begin:
            ans -= 1
            now_max = min(end, now_max)
        
        else:
            now_max = end
    
    print(ans)

main()



        
    
        
