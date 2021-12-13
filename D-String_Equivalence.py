





def dfs(n, count, ans_list):
    if n == count:
        return ans_list

    next_ans_list = []
    for i in range(len(ans_list)):
        char_list = ans_list[i]
        char_max = max(char_list)
        for j in range(char_max + 2):
            next_ans_list.append(char_list + [j])
        
        
        
    return dfs(n, count + 1, next_ans_list)
        
def main():
    n = int(input())
    ans_list = dfs(n, 1, [[0]])
    for i in range(len(ans_list)):
        ans = ''
        for j in range(n):
            ans += chr(97 + ans_list[i][j])
        
        print(ans)
        
if __name__ == '__main__':
    main()

    
    
    

    
    