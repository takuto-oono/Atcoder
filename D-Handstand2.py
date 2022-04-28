





def main():
    n = int(input())
    count = [[0 for _ in range(9)] for _ in range(9)]
    
    for i in range(1, n + 1):
        string = str(i)
        first = int(string[0])
        last = int(string[-1])
        
        if first == 0 or last == 0:
            continue
        
        count[first - 1][last - 1] += 1
    
    ans = 0
    for i in range(9):
        for j in range(9):
            ans += count[i][j] * count[j][i]
            
    print(ans)

if __name__ == '__main__':
    main()
