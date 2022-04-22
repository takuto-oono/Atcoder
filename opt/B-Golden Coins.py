x = int(input())
a = int(x // 500)
b = int((x % 500) / 5)

print(int(a * 1000 + b * 5))