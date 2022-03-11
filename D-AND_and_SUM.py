def is_x_y(a: int, s: int) -> bool:
    y = s - 2 * a
    x = a
    if y >= 0 and y & x == 0:
        return True

    return False

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        a, s = map(int, input().split())
        if is_x_y(a, s):
            print('Yes')
        else:
            print('No')
