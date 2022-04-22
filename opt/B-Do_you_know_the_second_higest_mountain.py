n = int(input())
D_s = []
D_t = []
for i in range(n):
    s, t = input().split()
    t = int(t)
    D_s.append(s)
    D_t.append(t)


D_t_new = sorted(D_t)
x = D_t_new[n - 2]
for i in range(n):
    if D_t[i] == x:
        print(D_s[i])
        exit()




