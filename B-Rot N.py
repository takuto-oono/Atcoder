n = int(input())
s = input()
x =[]
for i in range(len(s)):
    ord_si = ord(s[i])
    ord_si += n
    if ord_si > 90:
        ord_si = 64 + ord_si - 90
    x.append(chr(ord_si))

print(''.join(x))

    
