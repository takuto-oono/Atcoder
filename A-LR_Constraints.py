





def Initial_value_setting(Card, K):
    for i in range(len(K)):
        Card[K[i] - 1] = i + 1

def Creat_unavailable_list(CK):
    L = []
    for i in range(len(CK)):
        if CK[i][0] == 'L':
            L.append(i + 1)

    return L

def Calculation(l, Card, Unavailable_list):
    ans = 1
    for i in range(len(Card)):
        card = Card[i]
        if card == 0:
            ans *= l - len(Unavailable_list)
            ans %= 998244353

        else:
            if card in Unavailable_list:
                Unavailable_list.remove(card)

            else:
                Unavailable_list.append(card)



    return ans % 998244353


def main():
    n, l = map(int, input().split())
    C = []
    K = []
    CK = []
    for i in range(l):
        c, k = input().split()
        C.append(c)
        K.append(int(k))
        CK.append([c, int(k)])

    Card = [0 for _ in range(n)]
    Initial_value_setting(Card, K)

    Unavailable_list = Creat_unavailable_list(CK)

    print(Calculation(l, Card, Unavailable_list))



main()

