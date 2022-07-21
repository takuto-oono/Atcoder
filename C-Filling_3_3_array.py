def main():
    h1, h2, h3, w1, w2, w3 = map(int, input().split())
    ans = 0
    for a in range(1, 31):
        for b in range(1, 31):
            for d in range(1, 31):
                for e in range(1, 31):
                    c = h1 - a - b
                    f = h2 - d - e
                    g = w1 - a - d
                    h = w2 - b - e
                    i = w3 - c - f
                    if i + h + g == h3 and min(c, f, g, h, i) > 0:
                        ans += 1
    print(ans)


if __name__ == '__main__':
    main()
