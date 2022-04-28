N = int(input())
co = 0
for i in range(N):
    D1, D2 = map(int,input().split())
    if D1 == D2:
        co += 1
    else:
        co = 0

    if co >= 3:
        print('Yes')
        exit()
print('No')
