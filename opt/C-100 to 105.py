x = int(input())
a = x // 100
if x % 100 >= 0 and x % 100 <= 5 * a:
    print(1)
else:
    print(0)
    
