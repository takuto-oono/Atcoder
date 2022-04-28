





def main():
    n = int(input())
    csf_list = []
    for i in range(n - 1):
        c, s, f = map(int, input().split())
        csf_list.append([c, s, f])
        
    
    for i in range(n):
        if i == n - 1:
            print(0)
            break
        
        t = 0
        
        for j in range(i, n - 1):
            departure_time = max(t, csf_list[j][1])
            departure_time = (departure_time + csf_list[j][2] - 1) // csf_list[j][2] * csf_list[j][2]
            
            t = departure_time + csf_list[j][0]
        
        print(t)

if __name__ == '__main__':
    main()

    
    
            
    