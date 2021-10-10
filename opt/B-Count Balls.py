n,a,b = map((int,input().split())

balls_list = []
while len(balls_list) <= n:
    balls_list.append(['r'] * a)
    balls_list.append(['b'] * b)

new_list = balls_list[ :n]

from collections import Counter

count = Counter(new_list)

x = count['b']

print(x)
