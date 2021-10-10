





def main():
    a, b = map(int, input().split())
    ans = 0
    for i in range(256):
        if a^i == b:
            ans = i
            break

    print(ans)

main()
