H, W = map(int,input().split())
x = []
for i in range(H):
    a = input()
    x.append(a)

print('#' * (W + 2))
for i in range(H):
    print('#' + x[i] + '#')
print('#' * (W + 2))