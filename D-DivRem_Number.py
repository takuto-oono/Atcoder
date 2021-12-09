import math





def create_divisor_list(n):
    divisor_list = []
    n_sqrt = int(math.sqrt(n))
    for i in range(1, n_sqrt + 2):
        if n % i == 0:
            divisor_list.append(i)
            divisor_list.append(n // i)
        
    divisor_list = list(set(divisor_list))
    return divisor_list

def main():
    n = int(input())
    ans = 0
    divisor_list = create_divisor_list(n)
    
    for divisor in divisor_list:
        quotient = n // divisor - 1
        if divisor < quotient:
            ans += quotient
    
    print(ans)
    
if __name__ == '__main__':
    main()
