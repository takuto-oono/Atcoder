n = int(input())D = []for i in range(2 * n):    a, c = map(int, input().split())    D.append([a, c])D = sorted(D)R = []G = []B = []i = 0while (i < n):    if D[i][0] == D[i + 1][0] and D[i][1] != D[i + 1][1]:        i += 2    else: