N = int(input())
x = 0

for i in range(1,N + 1):
    if len(str(i)) % 2 == 1:
        x += 1

print(x)
