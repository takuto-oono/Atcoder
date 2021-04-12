n = int(input())
s = input()
x = 0
if n % 2 == 0:
    for i in range(int(n / 2)):
        if s[i] == s[i + int(n / 2)]:
            x += 1
elif n == 1:
    x = 100000

if x == int(n / 2):
    print('Yes')
else:
    print('No')
        