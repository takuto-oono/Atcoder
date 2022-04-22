





def Exchange(x, k):
    y = 0
    x_str = str(x)
    l = len(x_str)

    for i in range(l):
        y += int(x_str[i]) * k ** (l - i - 1)

    return y

def main():
    k = int(input())
    a, b = map(int, input().split())
    print(Exchange(a, k) * Exchange(b, k))

main()
