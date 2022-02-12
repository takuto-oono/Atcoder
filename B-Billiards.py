Sx, Sy, Gx, Gy = map(int,input().split())
ans = (Sy * Gx + Gy * Sx) / (Sy + Gy)
print(ans)