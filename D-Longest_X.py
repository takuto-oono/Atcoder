def main():
    s_string = input()
    k = int(input())
    ans = 0

    if k == 0:
        ans = 0
        cnt = 0
        for i in range(len(s_string)):
            if i == len(s_string) - 1:
                ans = max(cnt, ans)
                break

            if s_string[i] == 'X':
                cnt += 1
                continue

            if s_string[i] == '.':
                ans = max(cnt, ans)
                cnt = 0

        print(ans)
        exit()

    def two_pointers(s_string, k):
        l = 0
        r = 0
        ans = 0
        cnt = 0
        for i in range(len(s_string)):
            if i == len(s_string) - 1:
                ans = len(s_string)
                r = i
                break

            if s_string[i] == '.':
                cnt += 1

            if cnt == k:
                r = i
                ans = i + 1
                break

        x_cnt = ans
        while(True):
            l += 1
            x_cnt -= 1
            if l == len(s_string):
                break

            if s_string[l] == 'X':
                continue

            if s_string[l] == '.':

                while(True):
                    r += 1
                    if r >= len(s_string):
                        ans = max(x_cnt, ans)
                        break

                    if s_string[r] == '.':
                        x_cnt += 1
                        ans = max(ans, x_cnt)
                        break

                    if s_string[r] == 'X':
                        x_cnt += 1
                        continue

        return ans

    ans = two_pointers(s_string, k)
    print(ans)


if __name__ == '__main__':
    main()
