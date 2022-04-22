





def count(n, now, condidate_list):
    
    if now > n:
        return 0
    
    condidate_list.append(now)
    
    return count(n, now * 10 + 3, condidate_list) + count(n, now * 10 + 5, condidate_list) + count(n, now * 10 + 7, condidate_list) + 1
    
def main():
    n = int(input())
    condidate_list = []
    count(n, 0, condidate_list)
    ans = 0
    
    for condidate in condidate_list:
        if condidate > n:
            continue
        
        condidate_str = str(condidate)
        check_list = [0, 0, 0]
        
        for char in condidate_str:
            if char != '3' and char != '5' and char != '7':
                break
            
            if char == '3':
                check_list[0] = 1
            
            if char == '5':
                check_list[1] = 1
            
            if char == '7':
                check_list[2] = 1
            
            if sum(check_list) == 3:
                ans += 1
                break
            
    print(ans)
        
if __name__ == '__main__':
    main()
    
    
    
            