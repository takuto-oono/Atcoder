





def create_distance(i, j, x, y):
    return min(abs(j - i), abs(x - i) + abs(y - j) + 1)

def print_ans(ans_list):
    for ans in ans_list:
        print(ans)

def main():
    n, x, y = map(int, input().split())
    ans_list = [0 for _ in range(n - 1)]
    
    for i in range(n - 1):
        for j in range(i + 1, n):
            distance = create_distance(i + 1, j + 1, x, y)
            ans_list[distance - 1] += 1

    print_ans(ans_list)

if __name__ == '__main__':
    main()



        

        