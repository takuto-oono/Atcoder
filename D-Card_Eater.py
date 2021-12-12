





def detail_memo(memo):
    if memo % 2 == 0:
        return 0
    
    if memo % 2 == 1:
        return 1
    
def main():
    n = int(input())
    a_list = list(map(int, input().split()))
    
    
    b_list = [0 for _ in range(10 ** 5)]
    for a in a_list:
        b_list[a - 1] += 1
    
    ans = 0
    memo = 0
    for i in range(10 ** 5):
        b = b_list[i]
        if b == 0 or b == 1:
            continue
        
        if b % 2 == 1:
            b_list[i] = 1
            continue
        
        if b % 2 == 0:
            memo += 1
            b_list[i] = 1
            continue
        
    ans = sum(b_list) - detail_memo(memo)
    print(ans)
    
if __name__ == '__main__':
    main()
    