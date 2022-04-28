S_a = input()
S_b = input()
S_c = input()
a = 0
b = 0
c = 0
n = len(S_a) + len(S_b) + len(S_c)
next_turn = ''
for i in range(n + 3):
    if i == 0:
        next_turn = S_a[0]
        a += 1
    
    elif next_turn == 'a':
        if a == len(S_a):
            print('A')
            exit()
        else:
            next_turn = S_a[a]
            a += 1
    
    elif next_turn == 'b':
        if b == len(S_b):
            print('B')
            exit()
        else:
            next_turn = S_b[b]
            b += 1
    
    elif next_turn == 'c':
        if c == len(S_c):
            print('C')
            exit()
        else:
            next_turn = S_c[c]
            c += 1






