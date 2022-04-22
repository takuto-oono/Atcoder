def count_ans(n: int, s_string: str) -> None:
    i = 0
    ans = 0
    while(i < n - 1):
        if s_string[i] == s_string[i + 1]:
            j = i
            while(True):
                if j == n - 1:
                    if s_string[j] == s_string[i]:
                        j += 1

                    break

                if s_string[i] == s_string[j]:
                    j += 1

                else:
                    break

            # print(i, j)
            cnt = j - i
            ans += cnt * (cnt - 1) // 2
            i = j

        else:
            i += 1
    print(ans)


if __name__ == '__main__':
    n = int(input())
    s_string = input()
    count_ans(n, s_string)
