def main():
    k = int(input())
    k_bin = bin(k)
    ans = exchange(k_bin)
    print(ans)


def exchange(k_bin):
    ans = ''
    for k in k_bin:
        if k == '1':
            ans += '2'        
        if k == '0':
            ans += '0'

    return ans[1:]


if __name__ == '__main__':
    main()
