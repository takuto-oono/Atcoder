def input1():
    a, b = map(int, input().split())
    return a, b

def juge(a, b):
    if a == 0 and b > 0:
        ans = 'Silver'
    elif b == 0 and a > 0:
        ans = 'Gold'
    else:
        ans = 'Alloy'
    print(ans)

def main():
    a, b = input1()
    juge(a, b)

main()
