S = input()
k = int(input())
T = S
memo = 0
when_one = 0
for i in range(1, len(T)):
    if memo == 0 and T[i] == T[i - 1]:
        when_one += 1
        memo = 1
    else:
        memo = 0

T += S
when_two = 0
memo = 0
for i in range(1, len(T)):
    if memo == 0 and T[i] == T[i - 1]:
        when_two += 1
        memo = 1
    else:
        memo = 0

T += S
when_three = 0
memo = 0

for i in range(1, len(T)):
    if memo == 0 and T[i] == T[i - 1]:
        when_three += 1
        memo = 1
    else:
        memo = 0
if len(list(set(S))) == 1:
    ans = len(S) * k // 2

elif k == 1:
    ans = when_one
elif k == 2:
    ans = when_two
elif k == 3:
    ans = when_three
else:
    ans = when_one + (when_three - when_two) * (k - 1)

print(ans)
