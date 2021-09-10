





def main():
    xy = input()
    i = 0
    x = ''
    while(xy[i] != '.'):
        x += xy[i]
        i += 1
    y = int(xy[-1])


    ans = x
    if 0 <= y <= 2:
        ans += '-'
    elif 7 <= y <= 9:
        ans += '+'

    print(ans)

main()
