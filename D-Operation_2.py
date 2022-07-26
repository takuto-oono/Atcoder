from bisect import bisect_left
from typing import List, Generator


class Operation2:
    def __init__(self, n: int, a_list: List[int]) -> None:
        self.n = n
        self.a_list = sorted(a_list)
        self.a_cumulative_sum_list = [s for s in self.create_a_cumulative_sum_list()]

    def create_a_cumulative_sum_list(self) -> Generator[int, None, None]:
        result = 0
        for a in self.a_list:
            result += a
            yield result

    def main_operate(self, x: int) -> int:
        if x <= self.a_list[0]:
            return self.a_cumulative_sum_list[-1] - self.n * x
        if x >= self.a_list[-1]:
            return self.n * x - self.a_cumulative_sum_list[-1]

        i = bisect_left(self.a_list, x)
        return (2 * i - self.n) * x - 2 * self.a_cumulative_sum_list[i - 1] + self.a_cumulative_sum_list[-1]


def main():
    n, q = map(int, input().split())
    a_list = list(map(int, input().split()))
    operation2 = Operation2(n, a_list)
    for _ in range(q):
        print(operation2.main_operate(int(input())))


if __name__ == '__main__':
    main()
