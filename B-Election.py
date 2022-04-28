





def main():
    n = int(input())
    s_list = []
    for i in range(n):
        s = input()
        s_list.append(s)
        
    t_list = list(set(s_list))
    t_count = []
    
    for i in range(len(t_list)):
        c = 0
        for s in s_list:
            if s == t_list[i]:
                c += 1
            
        t_count.append(c)
    
    max_value = 0
    index = 0
    for i in range(len(t_list)):
        if t_count[i] >= max_value:
            max_value = t_count[i]
            index = i
        
    ans = t_list[index]
    
    print(ans)
    
if __name__ == '__main__':
    main()
    

            