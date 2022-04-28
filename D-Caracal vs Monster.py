H = int(input())
c = 0
ans = 0
while H > 1:
    H = H // 2
    c += 1
for i in range(c + 1):
    ans += 2 ** i
print(ans)

