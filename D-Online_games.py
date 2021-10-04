from collections import Counter





def main():
    n = int(input())
    C = Counter()
    
    for _ in range(n):
        a, b = map(int, input().split())

        C[a] += 1
        C[a + b] -= 1
    
    
    ans = [0 for _ in range(n + 1)]
    days = sorted(C.keys())
    pre_day = 0
    count = 0

    for day in days:
        ans[count] += day - pre_day
        count += C[day]
        pre_day = day
    
    print(*ans[1:])


        


if __name__ == '__main__':
    main()


