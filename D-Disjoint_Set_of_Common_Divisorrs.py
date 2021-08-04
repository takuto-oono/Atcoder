a, b = map(int, input().split())

def Prime_factor(n):
    P = []
    z = n
    for i in range(1, int(n ** 0.5) + 1):
        if z % i == 0:
            while(z % i == 0 and i > 1):
                z //= i
            P.append(i)
    return P

A = Prime_factor(a)
B = Prime_factor(b)

def check(A, B):
    ans = 0
    for i in A:
        for j in B:
            if i == j:
                ans += 1
                break
    return ans

print(check(A, B))


