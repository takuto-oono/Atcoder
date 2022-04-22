





def main():
    n = int(input())
    list_a = list(map(int, input().split()))
    m = 1000000007
    register = [0, 0, 0]
    ans = 1
    
    for i in range(len(list_a)):
        a = list_a[i]
        count = 0
        for j in range(3):
            if a == register[j]:
                count += 1
                
        ans *= count
        ans %= m
        for j in range(3):
            if a == register[j]:
                register[j] += 1
                break
            
    print(ans % m)
    
if __name__ == '__main__':
    main()
    

        

        