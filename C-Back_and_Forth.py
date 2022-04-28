





def main():
    sx, sy, tx, ty = map(int, input().split())
    x = tx - sx
    y = ty - sy
    ans = ''
    u = 'U'
    d = 'D'
    l = 'L'
    r = 'R'

    ans += u * y + r * x + d * y + l * x

    ans += l + u * (y + 1) + r * (x + 1) + d

    ans += r + d * (y + 1) + l * (x + 1) + u

    print(ans)

main()

