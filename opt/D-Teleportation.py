coordinate_list = []
ans_list = []


def factorial(n):
    factorial_dic = {}
    tmp = n
    for i in range(2, int(n ** 0.5) + 1):
        cnt = 0
        if tmp % i == 0:
            while(tmp % i == 0):
                cnt += 1
                tmp //= i
            factorial_dic[i] = cnt

    if tmp != 1:
        factorial_dic[tmp] = 1

    if len(factorial_dic) == 0:
        factorial_dic[tmp] = 1

    return factorial_dic


def full_search(n):
    for i in range(n):
        for j in range(n):
            if i == j:
                continue

            dx = coordinate_list[j][0] - coordinate_list[i][0]
            dy = coordinate_list[j][1] - coordinate_list[i][1]
            if dx == 0:
                dy //= abs(dy)
                ans_list.append([0, dy])
                continue
            
            if dy == 0:
                dx //= abs(dx)
                ans_list.append([dx, 0])
                continue
            
            ans_list.append(reduction_of_fraction(dx, dy))

def reduction_of_fraction(x, y):
    factorial_x_dic = factorial(abs(x))
    factorial_y_dic = factorial(abs(y))
    d = 1
    for key_x in factorial_x_dic:
        if key_x in factorial_y_dic:
            d *= key_x * min(factorial_x_dic[key_x], factorial_y_dic[key_x])

    return [x // d, y // d]


def count_ans_list():
    l = len(ans_list)
    cnt = l
    ans_list.sort()
    for i in range(l - 1):
        if ans_list[i] == ans_list[i + 1]:
            cnt -= 1
            
    print(cnt)


if __name__ == "__main__":
    n = int(input())
    for i in range(n):
        x, y = map(int, input().split())
        coordinate_list.append([x, y])

    full_search(n)
    count_ans_list()
