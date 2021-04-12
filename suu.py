A = [30, 20, 70, 50, 40, 40, 40, 40, 55, 60, 33, 33, 30, 50, 45, 90, 20, 50, 43, 70]
N = len(A)
ave_a = sum(A) / N
print(ave_a, N)
B = [45, 88, 75, 40, 65, 97, 43, 50, 35, 40, 77, 76, 43, 70, 23, 50, 63, 60, 65, 60]
ave_b = sum(B) / N
print(ave_b, len(B))

A = sorted(A)
B = sorted(B)
print((A[9] + A[10]) / 2)
print((B[9] + B[10]) / 2)
print(A[9], A[10], B[9], B[10])

import collections
mode_a = collections.Counter(A)
print(mode_a)
mode_b = collections.Counter(B)
print(mode_b)

C = [2, 4, 6, 4, 1, 2, 1]
n = sum(C)
D = []
for i in C:
    D.append(i / n)

print(D)

E = [25, 25, 35, 35, 35, 35, 45, 45, 45, 45, 45, 45, 55, 55, 55, 55, 65, 75, 75, 85]
nu = len(E)
ave_e = sum(E) / nu
print(ave_e, nu)
E = sorted(E)
print(E[9], E[10], (E[9] + E[10]) / 2)
mode_e = collections.Counter(E)
print(mode_e)

B_20, B_30, B_40, B_50, B_60, B_70, B_80, B_90 = 0, 0, 0, 0, 0, 0, 0, 0

for i in B:
    if 20 <= i < 30:
        B_20 += 1
    elif 30 <= i < 40:
        B_30 += 1
    elif 40 <= i < 50:
        B_40 += 1
    elif 50 <= i < 60:
        B_50 += 1
    elif 60 <= i < 70:
        B_60 += 1
    elif 70 <= i < 80:
        B_70 += 1
    elif 80 <= i < 90:
        B_80 += 1
    elif 90 <= i <= 100:
        B_90 += 1

B_20_90 = [B_20, B_30, B_40, B_50, B_60, B_70, B_80, B_90]
print(B_20_90)
soutaidosu = []
for i in B_20_90:
    soutaidosu.append(i / sum(B_20_90))
print(soutaidosu)

sum_B = B_20 * 25 + B_30 * 35 + B_40 * 45 + B_50 * 55 + B_60 * 65 + B_70 * 75 + B_80 * 85 + B_90 * 95
ave_B = sum_B / 20
print(ave_B)  

