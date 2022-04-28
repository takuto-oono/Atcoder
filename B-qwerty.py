




def exchange(p):
    p_chr = chr(p + 96)
    return p_chr

def main():
    P = list(map(int, input().split()))
    Ans = []
    for i in range(len(P)):
        Ans.append(exchange(P[i]))

    Ans = ''.join(Ans)
    print(Ans)

main()

