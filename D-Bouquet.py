





def main():
    n, a, b = map(int, input().split())
    mod = 10 ** 9 + 7
    ans = 2 ** n - 1
    
    def cmb(n, r, mod):
        x = 1
        for i in range(r):
            x *= (n - i)
            x *= pow(i + 1, mod - 2, mod)
            x %= mod
        
        return x
    
    a_cmb = cmb(n, a, mod) % mod
    b_cmb = cmb(n, b, mod) % mod
    
    ans -= a_cmb + b_cmb
    print(ans % mod)
    
if __name__ == '__main__':
    main()
