n = int(input())
A = list(map(int, input().split()))
Candidate_list = [i for i in range(min(A), max(A) + 1)]
ans = 10 ** 10
for i in range(len(Candidate_list)):
    cost = 0
    for j in range(n):
        cost += (Candidate_list[i] - A[j]) ** 2

    ans = min(ans, cost)
print(ans)


