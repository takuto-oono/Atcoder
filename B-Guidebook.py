N = int(input())
S_list = []
P_list = []
c = []

for i in range(N):
    S, P = input().split()
    S_list.append(S)
    P_list.append(int(P))

m = S_list
m = list(set(m))
m = sorted(m)

n = 0
a = []
b = []
for i in m:
    for j in range(N):
        if i == S_list[j]:
            a.append(j)
    n = len(a)
    if n != 1:
        for o in range(n):
            b.append(P_list[a[o]])
        b = sorted(b, reverse = True)
        for k in b:
            for l in range(N):
                if k == P_list[l]:
                    c.append(l)
    else:
        c.append(a[0])


    a = []
    b = []

for i in c:
    print(str(i + 1))


        
            



     

