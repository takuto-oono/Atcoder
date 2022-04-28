prime_list = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97, 101, 103, 107, 109, 113, 127, 131, 137, 139, 149, 151, 157, 163, 167, 173, 179, 181, 191, 193, 197, 199]

if __name__ == "__main__":
    a, b, c, d = map(int, input().split())
    winner = "Aoki"
    for x in range(a, b + 1):
        flag = True
        for y in range(c, d + 1):
            z = x + y
            if z in prime_list:
                flag = False
                break
        
        if flag:
            winner = "Takahashi"
            break
    
    print(winner)
