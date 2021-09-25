





def Full_search(l):
    Combination = []
    for i in range(2 ** l):
        bag = ''
        for j in range(l):
            if ((i >> j) & 1):
                bag += '1'
            else:
                bag += '0'

        Combination.append(int(bag))
    Combination.sort()
    print(Combination)
    return Combination

def main():
    N = input()
    l = len(N)
    Combination = Full_search(l)
    for i in Combination(1, 2 ** l - 1):
        st = str(Combination[i])
        num = ''
        c = 0
        for j in st:
            if j == 0:
                num += '9'
                c += 1
            else:
                num += '1'

        num = int(num)
        co_1 = 0
        for j in st:
            if j == '1':
                co_1 += 1
            else:
                break

        if num <= int(N):
            ans += co_1 * 




main()


