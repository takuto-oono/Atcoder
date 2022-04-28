S = input()
K = int(input())


def cal_cumulative_sum():
    cumulative_sum_list = [0]
    cnt = 0
    for s in S:
        if s == '.':
            cnt += 1
        cumulative_sum_list.append(cnt)
    return cumulative_sum_list


def main():
    cmulative_sum_list = cal_cumulative_sum()
    right = 0
    ans = 0
    for left in range(len(S)):
        while (right < len(S)) and (cmulative_sum_list[right + 1] - cmulative_sum_list[left] <= K):
            right += 1
        ans = max(ans, right - left)

    print(ans)


if __name__ == '__main__':
    main()
