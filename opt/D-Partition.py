





def make_divisors(n):
    lower_divisors, upper_divisors = [], []
    i = 1
    while i * i <= n:
        if n % i == 0:
            lower_divisors.append(i)
            if i != n // i:
                upper_divisors.append(n // i)
        
        i += 1
    
    return lower_divisors + upper_divisors[::-1]

def main():
    n, m = map(int, input().split())
    divisors = make_divisors(m)
    divisors.sort(reverse=True)
    
    for divisor in divisors:
        if divisor * n <= m:
            print(divisor)
            exit()

if __name__ == '__main__':
    main()
    