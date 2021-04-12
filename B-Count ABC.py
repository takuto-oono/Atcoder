N = int(input())
S = input()
x = 0
ans = 0
for i in S:
    if i == 'A':
        if x == 0:
            x = 1
        else:
            x = 0
        
    elif i == 'B':
        if x == 1:
            x = 2
        else:
            x = 0
    
    elif i == 'C':
        if x == 2:
            ans += 1
            x = 0
        else:
            x = 0
    else:
        x = 0
        

print(ans)
