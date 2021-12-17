





def binary_search(n):
    list_item = [i for i in range(1, n)]
    list_pattern = []
    for i in range(2 ** (n - 1)):
        bag = []
        for j in range(n - 1):
            if ((i >> j) & 1):
                bag.append(list_item[j])
                
        bag.append(n)
        
        list_pattern.append(bag)
    
    return list_pattern

def main():
    s = input()
    n = len(s)
    
    list_pattern = binary_search(n)
    ans = 0
    
    for pattern in list_pattern:
        now = 0
        for j in range(len(pattern)):
            ans += int(s[now: pattern[j]])
            now = pattern[j]
            
    print(ans)
    
if __name__ == '__main__':
    main()
