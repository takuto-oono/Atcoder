if __name__ == '__main__':
    n = int(input())
    a_list = list(map(int, input().split()))
    a_list = list(set(a_list))
    print(len(a_list))
