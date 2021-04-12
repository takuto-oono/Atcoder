N, M = map(int,input().split())
H = list(map(int,input().split()))
ans = [i for i in range(1, N + 1)]
for i in range(M):
    A, B = map(int,input().split())
    if H[A - 1] == H[B - 1]:
        if A in ans:    
            ans.remove(A)
        if B in ans:    
            ans.remove(B)
    elif H[A - 1] < H[B - 1]:
        if A in ans:
            ans.remove(A)
    else:
        if B in ans:
            ans.remove(B)
    
print(len(ans))

