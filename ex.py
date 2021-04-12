list = [i for i in range(5)]

def f(x):
    list[x] = 100

f(3)
print(list)
