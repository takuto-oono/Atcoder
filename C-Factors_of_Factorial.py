





def prime(n):
    primes = []
    for i in range(2, n + 1):
        primes.append(i)
        for j in range(2, i):
            if i % j == 0:
                primes.remove(i)
                break
        
    return primes

def prime_factorization(n, primes, prime_factorization_output):
    for i in range(len(primes)):
        p = primes[i]
        c = 0
        while(n % p == 0):
            n //= p
            c += 1
        
        if c > 0:
            if p in prime_factorization_output:
                prime_factorization_output[p] += c

            else:
                prime_factorization_output[p] = c
        
    

    

def main():
    n = int(input())
    
    if n == 1:
        print(1)
        exit()
        
    if n == 2:
        print(2)
        exit()
        
    prime_factorization_output = {}
    
    for i in range(2, n + 1):
        primes_i = prime(i)
        prime_factorization(i, primes_i, prime_factorization_output)
    
    ans = 1
    
    for v in prime_factorization_output.values():
        ans *= (v + 1)
    
    print(ans % (10 ** 9 + 7))
    
if __name__ == "__main__":
    main()
