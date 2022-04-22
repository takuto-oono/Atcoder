n = int(input())
Time_list = []
for i in range(5):
    t = int(input())
    Time_list.append(t)

time_min = min(Time_list)

ans = 5

if n // time_min == n / time_min:
    ans += n // time_min - 1
else:
    ans += n // time_min
print(ans)
