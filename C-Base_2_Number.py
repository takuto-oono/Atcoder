if __name__ == '__main__':
    n = int(input())
    ans = ''
    if n != 0:
        while(n != 0):
            memo = n % 2
            ans += str(memo)
            n -= memo
            n //= -2
    else:
        ans = '0'

    print(''.join(ans[::-1]))
