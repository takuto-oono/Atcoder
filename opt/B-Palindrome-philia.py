s  = input()
x = 0

for i in range(len(s)):
    j = len(s) - i - 1
    if s[i] != s[j]:
        x += 1 / 2
        
    

print((int(x)))