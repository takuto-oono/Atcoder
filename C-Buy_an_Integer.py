a, b, x = map(int, input().split())
n_condidate_list = [10 * i for i in range(19)]
memo = 0
for i in range(19):

    y = n_condidate_list[i]
    if a * y + b * (i + 1) > x:
        memo = y
        break
while (a * memo + b * len(str(memo)) > x):
    memo -= 1
if memo < 0:
    memo = 0
print(memo)

