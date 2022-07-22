from typing import List


class NumberBox:
    def __init__(self, a_list: List[List[str]], n: int) -> None:
        self.a_list = a_list
        self.n = n
        self.dirs = [
            [-1, -1],
            [-1, 0],
            [-1, 1],
            [0, -1],
            [0, 1],
            [1, -1],
            [1, 0],
            [1, 1]
        ]
        self.ans = 0
        self.find_ans()

    def find_ans(self) -> None:
        for i in range(self.n):
            for j in range(self.n):
                for dir in self.dirs:
                    y = i
                    x = j
                    num = int(self.a_list[i][j])
                    for k in range(self.n - 1):
                        y += dir[0]
                        x += dir[1]
                        y %= self.n
                        x %= self.n
                        num *= 10
                        num += int(self.a_list[y][x])
                    self.ans = max(self.ans, num)
        print(self.ans)


def main():
    n = int(input())
    a_list = []
    for _ in range(n):
        a_list.append(list(input()))
    NumberBox(a_list, n)


if __name__ == '__main__':
    main()
