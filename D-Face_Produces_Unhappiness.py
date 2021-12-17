





def main():
    n, k = map(int, input().split())
    list_s = list(input());
    
    count_change = 1
    for i in range(n - 1):
        if list_s[i] != list_s[i + 1]:
            count_change += 1
    
    count_change = max(1, count_change - 2 * k)
    ans = n - count_change
    print(ans)
    
if __name__ == '__main__':
    main()
