





def no_yes(before, now, check_list, i):
    if before == '#' and now == '#':
        return 
    if before == '#' and now == '.':
        check_list[i][0] = min(check_list[i][0], check_list[i - 1][1] + 1)
        return

    if before == '.':
        check_list[i][0] = min(check_list[i][0], check_list[i - 1][1] + 1)
        return
        
def no_no(before, now, check_list, i):
    if before == '#' and now == '.':
        return
    
    check_list[i][1] = min(check_list[i][1], check_list[i - 1][1])
    return

def yes_yes(before, now, check_list, i):
    if before == '#' and now == '#':
        return

    check_list[i][0] = min(check_list[i][0], check_list[i - 1][0] + 1)
    
def yes_no(before, now, check_list, i):
    if before == '#' and now == '.':
        return

    check_list[i][1] = min(check_list[i][1], check_list[i - 1][0])
    
    
        
def main():
    n = int(input())
    S = list(input())
    
    check_list = [[10 ** 8 for _ in range(2)] for _ in range(n)]
    
    check_list[0][0] = 1
    check_list[0][1] = 0
    
    for i in range(1, n):
        before = S[i - 1]
        now = S[i]
        
        no_yes(before, now, check_list, i)
        
        no_no(before, now, check_list, i)
        
        if before == '#':
            before = '.'
        
        else:
            before = '#'
            
        yes_no(before, now, check_list, i)
        
        yes_yes(before, now, check_list, i)
        
    print(min(check_list[n - 1][0], check_list[n - 1][1]))
    
if __name__ == '__main__':
    main()
    
        
        