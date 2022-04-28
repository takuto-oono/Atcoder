





def main():
    n, k = map(int, input().split())
    d_list = list(input().split())
    
    while(True):
        n_str = str(n)
        boolean = True
        for n_char in n_str:
            if n_char in d_list:
                boolean = False
                break
        
        if boolean:
            print(n)
            exit()
            
        n += 1
        
if __name__ == '__main__':
    main()
