a_list = []
b_list = []
n = 0
m = 0


def judge() -> bool:
    for b in b_list:
        flag = True
        for i, a in enumerate(a_list):
            if b == a:
                a_list.pop(i)
                flag = False
                break

        if flag:
            return False

    return True


if __name__ == '__main__':
    n, m = map(int, input().split())
    a_list = list(map(int, input().split()))
    b_list = list(map(int, input().split()))

    if judge():
        print('Yes')
    else:
        print('No')
