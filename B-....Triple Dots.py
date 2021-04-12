k = int(input())
s = input()

if len(s) <= k:
    print(s)
elif len(s) > k:
    print(s[: k] + '...')