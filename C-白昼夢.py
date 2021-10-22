





def main():
    S = input()
    vocabulary_list = ['dream', 'dreamer', 'erase', 'eraser']
    i = 0
    ans = 'YES'
    word = ''
    while(i < len(S)):
        if i + 5 > len(S):
            ans = 'NO'
            break

        if i + 5 == len(S):
            word = S[i: i + 5]
            if word != vocabulary_list[0] and word != vocabulary_list[2]:
                ans = 'NO'
            
            break

        

        if i + 7 == len(S):
            word = S[i: i + 7]
            if word != vocabulary_list[1]:
                ans = 'NO'
            
            break
        
        if i + 6 == len(S):
            word = S[i: i + 6]
            if word != vocabulary_list[3]:
                ans = 'NO'
            
            break

            
        word = S[i: i + 7]
        if word == vocabulary_list[1]:
            if S[i + 7] == 'e' or S[i + 7] == 'd':
                i += 7
                continue

        if word[0: 6] == vocabulary_list[3]:
            if S[i + 6] == 'e' or S[i + 6] == 'd':
                i += 6
                continue
        
        if word[0: 5] == vocabulary_list[0] or word[0: 5] == vocabulary_list[2]:
            i += 5
            continue

        ans = 'NO'
        break

    print(ans)

if __name__ == '__main__':
    main()




        
        


