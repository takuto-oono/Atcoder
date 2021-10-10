a, b = input().split()
a_sum = 0
b_sum = 0
for i in range(3):
    a_sum += int(a[i])
    b_sum += int(b[i])

ans = max(a_sum, b_sum)
print(ans)

