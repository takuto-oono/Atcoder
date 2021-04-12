A, B, C = map(int,input().split())
num = [A, B, C]

if A % 2 == 0 or B % 2 == 0 or C % 2 == 0:
    print(0)

else:
    num = sorted(num)
    print(num[0] * num[1])

    
