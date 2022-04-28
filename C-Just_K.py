def main():
    n, k = map(int, input().split())
    s_list = [[0 for _ in range(26)] for _ in range(n)]
    for i in range(n):
        s_string = list(input())
        for s in s_string:
            s_list[i][ord(s) - 97] += 1

    ans = 0
    for i in range(2 ** n):
        cnt = 0
        char_count_list = [0 for _ in range(26)]
        for j in range(n):
            if ((i >> j) & 1):
                for l in range(26):
                    char_count_list[l] += s_list[j][l]
        for l in range(26):
            if char_count_list[l] == k:
                cnt += 1
        ans = max(ans, cnt)
    print(ans)


if __name__ == '__main__':
    main()
