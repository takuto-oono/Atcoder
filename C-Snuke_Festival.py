





def main():
    n = int(input())
    a_list = list(map(int, input().split()))
    b_list = list(map(int, input().split()))
    c_list = list(map(int, input().split()))
    a_list.sort()
    b_list.sort()
    c_list.sort()
    a_index = -1
    c_index = -1
    ans = 0
    
    for i in range(n):
        b = b_list[i]
        while(True):
            if a_index == n - 1:
                break

            if a_list[a_index + 1] >= b:
                break

            a_index += 1
        
        while(True):
            if c_index == n - 1:
                break

            if c_list[c_index + 1] > b:
                break

            c_index += 1
            
        ans += (a_index + 1) * (n - c_index - 1)
    
    print(ans)
    
if __name__ == '__main__':
    main()

    