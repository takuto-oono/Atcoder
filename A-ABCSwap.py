xyz = list(map(int,input().split()))
xyz[0] ,xyz[1] = xyz[1],xyz[0]
xyz[0], xyz[2] = xyz[2], xyz[0]
print(*xyz)
