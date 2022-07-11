from math import radians, cos, sin


def main():
    a, b, d = map(int, input().split())
    rad = radians(d)
    print(a * cos(rad) - b * sin(rad), a * sin(rad) + b * cos(rad))


if __name__ == '__main__':
    main()
