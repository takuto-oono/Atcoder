def main():
    h, w = map(int, input().split())
    a_list = []
    for i in range(h):
        a = list(map(int, input().split()))
        a_list.append(a)
    
    ans_list = [[0 for _ in range(h)] for _ in range(w)]
    for i in range(w):
        for j in range(h):
            ans_list[i][j] = a_list[j][i]
    
    for i in range(w):
        print(*ans_list[i])
    
    

if __name__ == '__main__':
    main()
        
        