





def main():
    string_s = input()
    k = int(input())
    
    list_substring = []
    for al in range(97, 124):
        char = chr(al)
        
        memo = []
        for i in range(len(string_s)):
            if (string_s[i] == char):
                if i == len(string_s) - 1:
                    memo.append([124, i])
                
                else:
                    memo.append([ord(string_s[i + 1]), i])
                    
        memo.sort()
            
        for i in range(len(memo)):
            begin = memo[i][1]
            j = 1
            while(begin + j <= len(string_s)):
                list_substring.append(string_s[begin: begin + j])
                j += 1
            
            list_substring = list(set(list_substring))
            
            if (len(list_substring) >= k):
                list_substring.sort()
                print(list_substring[k - 1])
                exit()
                
if __name__ == '__main__':
    main()
    
            
            
            