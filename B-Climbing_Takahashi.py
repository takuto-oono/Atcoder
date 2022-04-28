

def main():
    n = int(input())
    h_list = list(map(int, input().split()))
    ans = h_list[0]
    for height in h_list[1:n]:
        if ans >= height:
            break

        if ans < height:
            ans = height

    print(ans)


if __name__ == '__main__':
    main()
