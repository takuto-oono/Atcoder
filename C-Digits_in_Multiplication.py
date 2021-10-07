import math





def f(a, b):
    a_st = str(a)
    b_st = str(b)
    return max(len(a_st), len(b_st))

def search(n):
    n_sqrt = int(math.sqrt(n)) + 1
    memo = 1
    for i in range(2, n_sqrt):
        if n % i == 0:
            memo = max(memo, i)
    
    return f(memo, n // memo)

def main():
    n = int(input())
    print(search(n))

if __name__ == '__main__':
    main()


