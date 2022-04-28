a_list = []

if __name__ == '__main__':
    a_list = list(map(int, input().split()))
    ans = a_list[a_list[a_list[0]]]
    print(ans)
