X = int(input())
a = []
c = []
if X % 2 == 1:
    while a == []:
        for i in range(3,X,2):
            b = X % i
            a.append(b)
        if 0 in a:
            a = []
            X += 1
        else:
            print(X)
elif X == 2:
    print(X)
else:
    X += 1
    while c == []:
        for i in range(3,X,2):
            d = X % i
            c.append(d)
        if 0 in c:
            c = []
            X += 1
        else:
            print(X)

    
         
        
