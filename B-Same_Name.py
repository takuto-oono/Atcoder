





def main():
    n = int(input())
    ST = []
    for i in range(n):
        s, t = input().split()
        ST.append([s, t])

    ans = 'No'
    ST.sort()

    for i in range(n - 1):
        j = i + 1

        while(ST[i][0] == ST[j][0]):
            if ST[i][1] == ST[j][1]:
                ans = 'Yes'
                break

            j += 1
            if j == n:
                break

    print(ans)

main()


