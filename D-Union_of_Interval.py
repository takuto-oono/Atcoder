from typing import List


class UnionOfInterval:
    def __init__(self, lr_list: List[List[int]]) -> None:
        self.lr_list = sorted(lr_list)
        self.intervals: List[List[int]] = []
        self.create_intervals()
        self.print_intervals()

    def create_intervals(self) -> None:
        interval: List[int] = [self.lr_list[0][0], self.lr_list[0][1]]
        for lr in self.lr_list:
            left, right = lr[0], lr[1]
            if left <= interval[1]:
                interval[1] = max(interval[1], right)
            else:
                self.intervals.append(interval)
                interval = lr
        self.intervals.append(interval)

    def print_intervals(self) -> None:
        for lr in self.intervals:
            print(*lr)


def main():
    n = int(input())
    lr_list = []
    for _ in range(n):
        l, r = map(int, input().split())
        lr_list.append([l, r])
    UnionOfInterval(lr_list)


if __name__ == '__main__':
    main()
