import string


class Rotation:
    def __init__(self, s: string, n: int) -> None:
        self.s = s
        self.first = 0
        self.n = n

    def rotate(self, x: int) -> None:
        x %= self.n
        if self.first >= x:
            self.first -= x
        else:
            x -= self.first
            self.first = self.n - x

    def print(self, x: int) -> None:
        if self.first + x <= self.n:
            print(self.s[self.first + x - 1])
        else:
            print(self.s[self.first + x - self.n - 1])


def main():
    n, q = map(int, input().split())
    s = input()
    rotation = Rotation(s, n)
    for _ in range(q):
        t, x = map(int, input().split())
        if t == 1:
            rotation.rotate(x)
        if t == 2:
            rotation.print(x)


if __name__ == '__main__':
    main()
