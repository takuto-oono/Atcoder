def main():
    n, a, b = map(int, input().split())
    p, q, r, s = map(int, input().split())
    codinate = [['.' for _ in range(s - r + 1)] for _ in range(q - p + 1)]
    y_max = q - p + 1
    x_max = s - r + 1

    for i in range(y_max):
        for j in range(x_max):
            y = p + i
            x = r + j
            if y - a == x - b:
                k = y - a
                if max(1 - a, 1 - b) <= k <= min(n - a, n - b):
                    codinate[i][j] = '#'
                    continue

            if y - a == b - x:
                k = y - a
                if max(1 - a, b - n) <= k <= min(n - a, b - 1):
                    codinate[i][j] = '#'
                    continue

    for i in range(y_max):
        print(''.join(codinate[i]))


if __name__ == '__main__':
    main()
