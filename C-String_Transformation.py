





def main():
    S = input()
    T = input()
    grammar_list = [[0 for _ in range(26)] for _ in range(26)]
    ans = 'Yes'


    for i in range(len(S)):
        s = S[i]
        t = T[i]

        s_int = ord(s) - ord('a')
        t_int = ord(t) - ord('a')

        grammar_list[s_int][t_int] = 1
        
    
    for i in range(26):
        c = 0
        for j in range(26):
            if grammar_list[i][j] == 1:
                c += 1
        
        if c > 1:
            ans = 'No'
            break
    
    for i in range(26):
        c = 0
        for j in range(26):
            if grammar_list[j][i] == 1:
                c += 1
        
        if c > 1:
            ans = 'No'
            break
    
    



    print(ans)


if __name__ == '__main__':
    main()





        