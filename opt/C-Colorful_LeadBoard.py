n = int(input())
Check =[0 for i in range(8)]
others = 0
A = list(map(int,input().split()))

for i in range(n):
    a = A[i]
    if 1 <= a <= 399:
        Check[0] += 1
    elif 400 <= a <= 799:
        Check[1] += 1
    elif 800 <= a <= 1199:
        Check[2] += 1
    elif 1200 <= a <= 1599:
        Check[3] += 1
    elif 1600 <= a <= 1999:
        Check[4] += 1
    elif 2000 <= a <= 2399:
        Check[5] += 1
    elif 2400 <= a <= 2799:
        Check[6] += 1
    elif 2800 <= a <= 3199:
        Check[7] += 1
    else:
        others += 1
ans_min = 0
for i in range(8):
    if Check[i] != 0:
        ans_min += 1
if others == n:
    print(1, n)
    exit()
ans_max = ans_min + others
print(ans_min, ans_max)


