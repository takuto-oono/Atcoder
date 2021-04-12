n, a, b, c, d = map(int, input().split())
S = input()

if '##' in S[a:c - 1] or '##' in S[b:d - 1]:
    print("No")
    exit()

if c < d:
    print('Yes')
else:
    if '...' in S[b - 2:d + 1]:
        print('Yes')
    else:
        print('No')

