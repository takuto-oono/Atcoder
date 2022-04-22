





def preparation(a, b):
    memo = [[i, 1] for i in range(a, b + 1)]
    return memo

def main():
    n = int(input())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))

    memo = [0 for i in range(A[0] - 1)] + [1 for _ in range(B[0] - A[0] + 1)] + [0 for _ in range(3000 - B[0])]

    for i in range(n):
        if i == 0:
            
            continue

        m = 0
        for j in range(A[i - 1] - 1, B[i]):
            m += memo[j]
            
            if A[i] <= j + 1 <= B[i]:
                memo[j] = m
                memo[j] %= 998244353
        
    
    print(sum(memo) % 998244353)

main()

        


            




            

        

