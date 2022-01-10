





mod = 10 ** 9 + 7
def combination(n, k):
    def modinv(x):
        return pow(x, mod - 2, mod)
    
    modinv_list = [-1 for _ in range(k + 1)]
    
    for i in range(1, k + 1):
        modinv_list[i] = modinv(i)
        
    def binomial(n, k):
        com = 1
        for i in range(k):
            com *= n - i
            com *= modinv_list[i + 1]
            com %= mod
        
        return com
    
    return binomial(n, k)

def main():
    n, k = map(int, input().split())
    
    for i in range(1, k + 1):
        com1 = combination(n - k + 1, i)
        com2 = combination(k - 1, i - 1)
        ans = com1 * com2 % mod
        print(ans)
        
if __name__ == '__main__':
    main()
    