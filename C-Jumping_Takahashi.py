

a_list = []
b_list = []


def judge(n, x):
    a_sum = sum(a_list)
    b_sum = sum(b_list)
    dif_list = [b_list[i] - a_list[i] for i in range(n)]

    if a_sum > x:
        return False

    if b_sum < x:
        return False

    if a_sum == x or b_sum == x:
        return True

    y = x - a_sum
    dp = [[False for _ in range(y + 1)] for _ in range(n + 1)]

    for i in range(n + 1):
        dp[i][0] = True

    for i in range(n):
        for j in range(y + 1):
            if j - dif_list[i] >= 0:
                dp[i + 1][j] = dp[i + 1][j] or dp[i][j - dif_list[i]]

            dp[i + 1][j] = dp[i + 1][j] or dp[i][j]

    return dp[n][y]


if __name__ == '__main__':
    n, x = map(int, input().split())
    for _ in range(n):
        a, b = map(int, input().split())
        a_list.append(a)
        b_list.append(b)

    if judge(n, x):
        print('Yes')
    else:
        print('No')
