





def main():
    n = int(input())
    D = list(map(int, input().split()))
    m = 998244353
    if D[0] != 0:
        print(0)
        exit()

    C = [0 for _ in range(n)]
    for d in D:
        C[d] += 1
    
    if C[0] != 1:
        print(0)
        exit()
    
    

    
    ans = 1
    
    for i in range(n - 1):
        c_0 = C[i]
        c_1 = C[i + 1]
        
        

        if c_1 == 0 and c_0 == 0:
            continue
        
        if c_0 == 0 and c_1 != 0:
            print(0)
            exit()
        
        if c_0 != 0 and c_1 == 0:
            continue


        ans *= (c_0 ** c_1) % m

    print(ans % m)
    

if __name__ == "__main__":
    main()


    

