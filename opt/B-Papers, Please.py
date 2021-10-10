n = int(input())
a = list(map(int,input().split()))
even_list = []
for i in range(n):
    if a[i] % 2 == 0:
        even_list.append(a[i])

x = 0
for m in range(len(even_list)):
    if even_list[m] % 3 == 0 or even_list[m] % 5 == 0:
        x += 1

if  x == len(even_list):
    print('APPROVED')

else:
    print('DENIED')
        