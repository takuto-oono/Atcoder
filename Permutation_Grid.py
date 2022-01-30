def main():
    n = int(input())
    r_list = list(map(int, input().split()))
    c_list = list(map(int, input().split()))
    q = int(input())
    ans = ''

    for i in range(q):
        y, x = map(int, input().split())
        y -= 1
        x -= 1
        if r_list[y] + c_list[x] >= n + 1:
            ans += '#'

        else:
            ans += '.'

    print(ans)

if __name__ == '__main__':
    main()
