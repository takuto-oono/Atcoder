def main():
    n, m = map(int, input().split())
    b_list = []
    for i in range(n):
        b = list(map(int, input().split()))
        b_list.append(b)

    def judge(n, m, b_list):
        b = b_list[0][0]
        y = 0
        x = 0
        for j in range(1, 8):
            if (b - j) % 7 == 0:
                y = (b - j) // 7
                x = j - 1
                break
            
        if 7 - x < m:
            return False
        
        for i in range(n):
            for j in range(m):
                if b_list[i][j] != (y + i) * 7 + x + j + 1:
                    return False
        
        return True


    if judge(n, m, b_list):
        print('Yes')
    else:
        print('No')


if __name__ == '__main__':
    main()
