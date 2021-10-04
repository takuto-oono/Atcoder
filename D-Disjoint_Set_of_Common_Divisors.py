import math





def main():
    a, b = map(int, input().split())
    g = math.gcd(a, b)
    prime_factors = [1]
    x = g
    for i in range(2, int(math.sqrt(g)) + 2):
        if x == 1:
            break
        if x % i != 0:
            continue

        prime_factors.append(i)
        y = x // i
        while(x % i == 0):
            x //= i
    
    if x > 1:
        prime_factors.append(x)
    
    ans = len(prime_factors)
    print(ans)

main()

        
        


