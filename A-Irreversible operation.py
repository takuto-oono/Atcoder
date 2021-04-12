S = input()
x = 0
y = 0
N = len(S)
ans = N
def even(ans):
    for i in range(N // 2):
        y = N // 2
        if S[i] == S[i + y + 1]:
            x += 1
        if x == y:
            print(ans)
        else:
            
