





def main():
    n = int(input())
    ab_list = []
    sum_time = 0
    total_list = [0]
    for i in range(n):
        a, b = map(int, input().split())
        ab_list.append([a, b, a / b])
        sum_time += a / b
        total_list.append(sum_time)
    
    sum_time /= 2
    merging_doukasen = 0
    for i in range(n):
        if total_list[i] >= sum_time:
            merging_doukasen = i
            break

        
    
    time = sum_time - total_list[merging_doukasen - 1]
    ans = 0
    for i in range(merging_doukasen - 1):
        ans += ab_list[i][0]
    
    ans += ab_list[merging_doukasen][0] * (time / ab_list[merging_doukasen][2])

    print(ab_list)
    print(total_list)
    print(merging_doukasen)

    print(ans)

main()




