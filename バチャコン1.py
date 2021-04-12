x_list= list(map(int, input().split()))
u_list = input().split()

if 'BTC' in u_list:
    i = u_list.index('BTC')
    print(i)