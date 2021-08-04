def input1():
    a, b = map(int, input().split())
    return a, b

def calculation(a, b):
    ans = (a - b) / 3 + b
    print(ans)

def main():
    a, b = input1()
    calculation(a, b)

main()
