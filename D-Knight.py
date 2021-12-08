from functools import reduce
import math





def find_combination(x, y):
    s = -1
    t = -1
    for i in range(x + 1):
        if 2 * i > x:
            return False
        
        j = x - 2 * i

        if y == i + 2 * j:
            s = i
            t = j
            return s, t
    
    return False

def cmb(n, r):
    mod = 10 ** 9 + 7
    if r == 0:
        return 1
    numerator = reduce(lambda x, y: x * y % mod, [n - r + i + 1 for i in range(r)])
    denominator = reduce(lambda x, y: x * y % mod, [i + 1 for i in range(r)])
    return numerator * pow(denominator, mod - 2, mod) % mod



    

def main():
    x, y = map(int, input().split())
    s = 0
    t = 0
    m = 10 ** 9 + 7
    
    
    if find_combination(x, y) == False:
        print(0)
    
    else:
        s, t = find_combination(x, y)
        ans = cmb(s + t, s)
        
        print(ans)
        
if __name__ == '__main__':
    main()
    
