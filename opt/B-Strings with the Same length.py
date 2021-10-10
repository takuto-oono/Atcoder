n = int(input())
s , t = input().split()

x = []
for i in range(n):
    x.append(s[i])
    x.append(t[i])

print(''.join(x))