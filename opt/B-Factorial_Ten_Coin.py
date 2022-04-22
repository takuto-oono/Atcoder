p = int(input())

def factorial(n):
    ans = 1
    for i in range(1, n + 1):
        ans *= i
    return ans

C = []
for i in range(1, 11):
    C.append(factorial(i))



i = 0
ans = 0

while(p != 0):
    if C[10 - 1 - i] <= p:
        ans += p // C[10 - 1 - i]
        p -= (p // C[10 - 1 - i]) * C[10 - 1 - i]

    i += 1




print(ans)
























