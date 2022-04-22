def main():
    a, b, k = map(int, input().split())
    ans = 0
    while(True):
        if a >= b:
            break
        ans += 1
        a *= k

    print(ans)


if __name__ == '__main__':
    main()
