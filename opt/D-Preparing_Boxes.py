





def prime(n):
    primes = []
    for i in range(2, n + 1):
        primes.append(i)
        for j in range(2, i):
            if i % j == 0:
                primes.remove(i)
                break
        
    return primes

def main():
    n = int(input())
    A = list(map(int, input().split()))
    
    B = [-1 for i in range(n)]
    primes = prime(n)
    for i in primes:
        j = 2 * i - 1
        memo = [0]
        while(j < n):
            if A[j] == A[j - i]:
                memo.append(0)
            else:
                memo.append(1)
            j += i
        
        memo2 = []
        sum = 0
        for m in memo:
            sum += m
            memo2.append(sum % 2)
        
        if memo2[-1] != A[j - i]:
            for k in range(len(memo2)):
                memo2[k] = (memo2[k] + 1) % 2
        
        for k in range(len(memo2)):
            x = i * (k + 1) - 1
            if B[x] == -1 or B[x] == memo2[k]:
                B[x] = memo2[k]
            
            else:
                print(-1)
                exit()
    
    sum = 0
    for i in range(n):
        sum += B[i]
        
    if sum % 2 == A[0]:
        B[0] = 1
    else:
        B[0] = 0
        
    
    m = 0
    for i in range(n):
        if B[i] == 1:
            m += 1
            
    if m == 0:
        print(0)
        exit()
    
    print(m)
    print(*B)
    
main()
