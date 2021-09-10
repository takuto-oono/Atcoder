
def main():
    a, b = map(int, input().split())
    m = b // 2 + 1
    ans = 1
    for i in range(1,m + 1):
        y = m - i + 1
        c = 0
        x = a
        while(x <= b):
            if x % y == 0:
                c += 1
            x += 1
            if c == 2:
                break
        if c == 2:
            ans = y
            break

    print(ans)

main()





