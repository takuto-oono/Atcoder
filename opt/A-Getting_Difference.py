import math





def main():
    n, k = map(int, input().split())
    a_list = list(map(int, input().split()))
    a_gcd = 0
    for i in range(n):
        a_gcd = math.gcd(a_gcd, a_list[i])
    
    a_max = max(a_list)
    if k % a_gcd == 0 and k / a_gcd <= a_max and k <= a_max:
        ans = 'POSSIBLE'
    
    else:
        ans = 'IMPOSSIBLE'
    
    print(ans)
    
main()

    