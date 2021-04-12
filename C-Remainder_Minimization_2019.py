l, r = map(int, input().split())
dis = r - l + 1

L = l % 2019
R = r % 2019

reminder = []
i = L
while(i != R):
    if i == 2018:
        reminder.append(i)
        i = 0
    else:
        reminder.append(i)
        i += 1
reminder.append(R)


if dis >= 2019:
    ans = 0
elif dis < 2019:
    ans = 3000
    l = len(reminder)
    for i in range(l - 1):
        for j in range(i + 1, l):
            ans = min(((reminder[i] * reminder[j]) % 2019), ans)




print(ans)




