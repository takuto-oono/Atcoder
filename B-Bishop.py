import math
def man(h, w):
    if h == 1 or w == 1:
        return 1
    else:
        return math.ceil(h * W / 2)
H, W = map(int,input().split())
print(man(H, W))