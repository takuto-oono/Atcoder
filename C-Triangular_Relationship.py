import math




def f(k, m, n):
    c = 0
    for i in range(1, n + 1):
        if i % k == m:
            c += 1
    
    return c

def main():
    n, k = map(int, input().split())
    
    ans = 0
    if k % 2 == 0:
        m = k // 2
        ans += f(k, m, n) ** 3
    
    m = 0
    ans += f(k, m, n) ** 3
    
    print(ans)
    
if __name__ == '__main__':
    main()


