





from itertools import count


def main():
    n, m = map(int, input().split())
    count_list = [0 for _ in range(n)]
    for _ in range(m):
        a, b = map(int, input().split())
        count_list[a - 1] += 1
        count_list[b - 1] += 1
    
    ans = True
    for i in range(n):
        if count_list[i] % 2 == 1:
            ans = False
            break

    if ans:
        print('YES')
    else:
        print('NO')

if __name__ == '__main__':
    main()
