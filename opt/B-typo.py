





def Juge(S, T):
    n = len(S)
    M = []
    for i in range(n):
        if S[i] != T[i]:
            M.append(i)

    l = len(M)
    if l > 2:
        return False
    
    elif l == 0:
        return True
    
    elif l == 1:
        return False
    
    elif l == 2:
        m1 = M[0]
        m2 = M[1]
        if m2 - m1 != 1:
            return False
        
        if S[m2] != T[m1] or S[m1] != T[m2]:
            return False
        
        return True

def main():
    S = input()
    T = input()

    if Juge(S, T):
        print('Yes')
    
    else:
        print('No')

main()

