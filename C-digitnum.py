def main():
    n = int(input())

    def arithmetical_progression(n):
        return (1 + n) * n // 2

    def cal_main(n):
        m = 998244353
        criterion = [1, 9]
        ans = 0
        while(criterion[1] <= n):
            print(criterion)
            ans += arithmetical_progression(criterion[1] - criterion[0] + 1)
            criterion[0] *= 10
            criterion[1] = criterion[1] * 10 + 9

        criterion[1] = n
        print(criterion)
        ans += arithmetical_progression(criterion[1] - criterion[0] + 1)
        print(ans % m)

    cal_main(n)


if __name__ == '__main__':
    main()
