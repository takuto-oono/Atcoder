A, B, C = map(int,input().split())
ans = 0

while A != B or A != C or B != C:
    num = [A, B, C]
    num = sorted(num)
    if num[0] == num[1]:
        num[0] += 1
        num[1] += 1
    
    else:
        num[0] += 2
    
    ans += 1
    A = num[0]
    B = num[1]
    C = num[2]

print(ans)