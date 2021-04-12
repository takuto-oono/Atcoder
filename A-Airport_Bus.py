n, c, k = map(int, input().split())
T = []
ans = 0
number_occupants = 0
wait_start_time = 10 ** 12
for i in range(n):
    t = int(input())
    T.append(t)

T = sorted(T)
if c == 1:
    print(n)
    exit()

for i in range(n):
    t = T[i]
    if t - wait_start_time > k:
        ans += 1
        wait_start_time = 10 ** 12
        number_occupants = 0
    if number_occupants == 0:
        number_occupants = 1
        wait_start_time = t
    else:
        number_occupants += 1
        if number_occupants == c:
            ans += 1
            number_occupants = 0
            wait_start_time = 10 ** 12


    if t - wait_start_time == k:
        ans += 1
        wait_start_time = 10 ** 12
        number_occupants = 0

    if i == n - 1:
        ans += 1

print(ans)
