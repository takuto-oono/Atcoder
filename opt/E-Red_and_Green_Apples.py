





def main():
    x, y, a, b, c = map(int, input().split())
    p_list = list(map(int, input().split()))
    q_list = list(map(int, input().split()))
    r_list = list(map(int, input().split()))
    
    p_list.sort(reverse=True)
    q_list.sort(reverse=True)
    r_list = sorted(r_list, reverse=True)
    
    pq_list = [p_list[i] for i in range(x)] + [q_list[i] for i in range(y)]
    pq_list.sort()
    
    for i in range(c):
        if pq_list[i] >= r_list[i]:
            break
        
        pq_list[i] = r_list[i]
        
    ans = 0
    for i in range(x + y):
        ans += pq_list[i]
        
    print(ans)

if __name__ == '__main__':
    main()

    
    
    