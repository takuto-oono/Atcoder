





def Excluive_OR_sum(x):
    if x % 2 == 1:
        y = (x + 1) // 2
        if y % 2 == 0:
            return 0
        
        else:
            return 1
    
    else:
        y = x // 2
        if y % 2 == 0:
            return (0 ^ x)
        
        else:
            return (1 ^ x)
        
    
        
        
def main():
    a, b = map(int, input().split())
    
    ans = Excluive_OR_sum(a - 1) ^ Excluive_OR_sum(b)
    print(ans)
    
if __name__ == '__main__':
    main()

    
    