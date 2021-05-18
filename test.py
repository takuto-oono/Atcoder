n = int(input())
S = input()
T = input()
ans = 0
memo = -1
memo_2 = 0


for i in range(n):
    if i == n - 1:
        if memo == -1 and S[i] == T[i]:
            print(ans)
        else:
            if memo == '0':
                if S[i] == '1' and T[i] == '0':
                    ans += 1
                    print(ans)
                else:
                    print(-1)
            elif memo == '1':
                if S[i] == '0' and T[i] == '1':
                    ans += 1
                    print(ans)
                else:
                    print(-1)

    elif memo == -1:
        if S[i] == T[i]:
            continue
        else:
            memo = S[i]

    elif memo == '0':
        if S[i] == memo:
            memo_2 += 1

        else:
            if S[i + 1] == memo:
                ans += memo_2 + 1
                if memo_2 > 0:
                    memo_2 -= 1


                if T[i] == '0' and memo_2 == 0:

                    memo = -1
                else:
                    memo = '0'

            elif S[i] != T[i]:
                ans += memo_2 + 1
                if memo_2 > 0:
                    memo_2 -= 1

                if memo_2 == 0:
                    memo = -1

    elif memo == '1':
        if S[i] == '1':
            continue
        else:
            ans += 1
            if T[i] == '0':
                memo = '1'
            else:
                memo = -1

    print(i, ans, memo, memo_2)



