ABCD = list(map(int,input().split()))
x = sum(ABCD) / 2
ABCD.append(0)

for i in range(5):
    for j in range(5):
        if i != j:
            if x == ABCD[i] + ABCD[j]:
                print('Yes')
                exit()
print('No')


