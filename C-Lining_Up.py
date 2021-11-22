





def main():
    n = int(input())
    A = list(map(int, input().split()))
    
    A = sorted(A)
    
    jugement = True

    if n % 2 == 0:
        for i in range(n - 1):
            if i % 2 == 0:
                if A[i] != A[i + 1] or A[i] % 2 == 0:
                    jugement = False
                    break
    
    else:
        if A[0] != 0:
            jugement = False
        
        for i in range(1, n - 1):
            if i % 2 == 1:
                if A[i] != A[i + 1] or A[i] % 2 == 1:
                    jugement = False
                    break
    
    if jugement:
        print(2 ** (n // 2) % (10 ** 9 + 7))
    
    else:
        print(0)
    
if __name__ == '__main__':
    main()

            
            