def main():
    n = int(input())
    num_list = [0 for _ in range(n * 2 + 1)]
    for i in range(n):
        for j, f in enumerate(num_list):
            if f == 0:
                print(j + 1)
                num_list[j] = 1
                break

        m = int(input())
        num_list[m - 1] = 1

    for i, f in enumerate(num_list):
        if f == 0:
            print(i + 1)
            break
        
    e = int(input())
    if e == 0:
        exit()


if __name__ == '__main__':
    main()
