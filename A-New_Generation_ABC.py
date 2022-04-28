def juge(n):
    if 1 <= n <= 125:
        return 4
    elif 126 <= n <= 211:
        return 6
    else:
        return 8

def main():
    n = int(input())
    ans = juge(n)
    print(ans)

main()
