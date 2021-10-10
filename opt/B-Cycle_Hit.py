





def main():
    S = []
    for i in range(4):
        s = input()
        S.append(s)

    S.sort()


    T = ['2B', '3B','H', 'HR']
    if S == T:
        print('Yes')
    else:
        print('No')

main()

