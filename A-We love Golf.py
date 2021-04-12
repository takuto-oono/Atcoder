K = int(input())
A,B = map(int,input().split())

for i in range(1,1000):
    x = K * i
    if A <= x <= B:
        print('OK')
        exit()
    else:
        continue

print('NG')



    




