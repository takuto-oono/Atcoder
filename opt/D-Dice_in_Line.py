def Sum_Expected_Value(x, k):
    return (k + x) / 2

n, k = map(int,input().split())
P = list(map(int,input().split()))


candidate = sum(P[0:k])
Candidates = [candidate]



for i in range(k, n):
    candidate = candidate + P[i] - P[i - k]
    Candidates.append(candidate)
    

x = max(Candidates)

ans = Sum_Expected_Value(x, k)
print(ans)








