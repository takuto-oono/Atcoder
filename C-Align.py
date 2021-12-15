





def main():
    n = int(input())
    a_list = []
    for i in range(n):
        a = int(input())
        a_list.append(a)
        
    a_list.sort()
    a_large = []
    a_small = []
    condidate1 = 0
    
    
    for i in range(n):
        j = n - i - 1
        if i == j:
            a_small.append(a_list[i])
            break

        if i > j:
            break

        a_small.append(a_list[i])
        a_large.append(a_list[j])
        
    if n % 2 == 0:
        for i in range(len(a_large)):
            if i == len(a_large) - 1:
                condidate1 += a_large[i]
                break
            
            condidate1 += 2 * a_large[i]
            
        for i in range(len(a_small)):
            if i == len(a_small) - 1:
                condidate1 -= a_small[i]
                continue
            
            condidate1 -= 2 * a_small[i]
    
    if n % 2 == 1:
        for i in range(len(a_large)):
            condidate1 += 2 * a_large[i]
            
        for i in range(len(a_small)):
            if i == len(a_small) - 1 or i == len(a_small) - 2:
                condidate1 -= a_small[i]
                continue
                
            condidate1 -= 2 * a_small[i]
    
    a_large = []
    a_small = []
    condidate2 = 0
    
    for i in range(n):
        j = n - i - 1
        if i == j:
            a_large.append(a_list[i])
            break

        if i > j:
            break

        a_small.append(a_list[i])
        a_large.append(a_list[j])
        
    condidate2 = 0
    if n % 2 == 0:
        for i in range(len(a_large)):
            if i == len(a_large) - 1:
                condidate2 += a_large[i]
                break
            
            condidate2 += 2 * a_large[i]
            
        for i in range(len(a_small)):
            if i == len(a_small) - 1:
                condidate2 -= a_small[i]
                continue
            
            condidate2 -= 2 * a_small[i]
    
    if n % 2 == 1:
        for i in range(len(a_large)):
            if i == len(a_large) - 1 or i == len(a_large) - 2:
                condidate2 += a_large[i]
                continue
            
            condidate2 += 2 * a_large[i]
            
        for i in range(len(a_small)):
            condidate2 -= 2 * a_small[i]
            
    ans = max(condidate1, condidate2)
    print(ans)
    
if __name__ == '__main__':
    main()
