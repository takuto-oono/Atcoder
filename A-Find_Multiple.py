





def Find(a, b, c):
    x = c
    while(x <= b):
        if a <= x <= b:
            return x

        else:
            x += c

    return -1
def main():
    a, b, c = map(int, input().split())
    print(Find(a, b, c))

main()
