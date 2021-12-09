





def judge(C, try_times):
    a_count = 0
    b_count = 0
    
    for c in C:
        if c == 0:
            continue
        
        if c < 0:
            if c % 2 == 0:
                a_count += -c // 2
                continue
            
            if c % 2 == 1:
                a_count += (-c + 1) // 2
                b_count += 1
                continue
        
        if c > 0:
            b_count += c
            continue
        
    if (a_count > try_times) or (b_count > try_times):
        return False

    if (try_times - b_count) == 2 * (try_times - a_count):
        return True

    return False
        
def main():
    n = int(input())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))
    
    C = [A[i] - B[i] for i in range(n)]
    
    try_times = sum(B) - sum(A)
    ans = judge(C, try_times)
    
    if ans:
        print('Yes')
    
    else:
        print('No')
    
if __name__ == '__main__':
    main()

