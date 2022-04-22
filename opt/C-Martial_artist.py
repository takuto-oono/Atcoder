def create_is_used_list(skill_list, n):
    is_used_list = [False for _ in range(n)]
    is_used_list[n - 1] = True

    for i, skills in enumerate(reversed(skill_list)):
        if is_used_list[n - i - 1]:
            for skill in skills:
                is_used_list[skill - 1] = True

    return is_used_list


def cal_total_time(is_used_list, time_list):
    ans = 0
    for i, is_used in enumerate(is_used_list):
        if is_used:
            ans += time_list[i]

    print(ans)


if __name__ == '__main__':
    n = int(input())
    t_list = []
    a_list = []
    for i in range(n):
        tka = list(map(int, input().split()))
        t = tka.pop(0)
        k = tka.pop(0)
        t_list.append(t)
        a_list.append(tka)

    cal_total_time(create_is_used_list(a_list, n), t_list)
