A, B, C, K = map(int,input().split())
ans = A - B
if abs(ans) > 10 ** 18:
    print('Unfair')
elif K % 2 == 1:
    ans *= -1
    print(ans)
else:
    print(ans)