N = int(input())
a, w, t, r = 0, 0, 0, 0
for _ in range(N):
    S = input()
    if S == 'AC':
        a += 1
    elif S == 'WA':
        w += 1
    elif S == 'TLE':
        t += 1
    else:
        r += 1
print('AC x ' + str(a))
print('WA x ' + str(w))
print('TLE x ' + str(t))
print('RE x ' + str(r))
