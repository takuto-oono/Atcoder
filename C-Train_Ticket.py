num = input()
num = list(num)

all_patterns = 2 ** 3
for i in range(all_patterns):
    condidate = num[0]
    condidate = int(condidate)
    hugou = ''
    for j in range(3):
        if (i >> j) & 1:
    
            z = num[j + 1]
            condidate += int(z)
            hugou += '+'
        else:
            z = num[j + 1]
            condidate -= int(z)
            hugou += '-'
    if condidate == 7:
        ans = num[0] + hugou[0] + num[1] + hugou[1] + num[2] + hugou[2] + num[3] + '=7'
        print(ans)
        exit()

print(num[0] + '+' + num[1] + '+' + num[2] + '+' + num[3] + '=7')

