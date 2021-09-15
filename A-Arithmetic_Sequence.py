





def Number_of_process(x):
    ans = 0
    y = x
    if y >= 0:
        ans += y

    else:
        ans += int(abs(y) / 2 + 0.5)
        if y % 2 == 1:
            ans += 1

    return ans


def main():
    A = list(map(int, input().split()))
    x = 2 * A[1] - A[0] - A[2]
    print(Number_of_process(x))

main()
