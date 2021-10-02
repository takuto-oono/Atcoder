





def Integer_convert(X):
    x = 0
    X_len = len(X)
    for i in range(X_len):
        x += 10 ** (X_len - i - 1) * X[i]
    
    return x
    
def Full_search(N):
    ans = 0
    n = len(N)
    for i in range(2 ** n):
        B1 = []
        B2 = []
        for j in range(n):
            if ((i >> j) & 1):
                B1.append(N[j])
            
            else:
                B2.append(N[j])
            
        B1.sort(reverse=True)
        B2.sort(reverse=True)
        l = min(len(B1), len(B2))
        if l == 0 or B1[0] == 0 or B2[0] == 0:
            continue

        b1 = Integer_convert(B1)
        b2 = Integer_convert(B2)
        ans = max(ans, b1 * b2)
        
    
    return ans



def main():
    N = list(input())
    for i in range(len(N)):
        N[i] = int(N[i])

    print(Full_search(N))

main()


    
    
