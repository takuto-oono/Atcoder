n = int(input())
BA = []
for i in range(n):
    a, b = map(int, input().split())
    BA.append([b, a])

elapsed_time = 0
BA = sorted(BA)

for i in range(n):
    elapsed_time += BA[i][1]
    if elapsed_time <= BA[i][0]:
        continue
    else:
        print('No')
        exit()
print('Yes')



