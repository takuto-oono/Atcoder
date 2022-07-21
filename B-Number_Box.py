from typing import List

class NumberBox:
    def __init__(self, a_list: List[List[int]], n: int) -> None:
        self.a_list = a_list
        self.n = n
        self.is_exist = {}
        self.dir = [
            [-1, -1],
            [-1, 0],
            [-1, 1],
            [0, -1],
            [0, 1],
            [1, -1],
            [1, 0],
            [1, 1],
        ]
        for i in range(1111, 10000):
            self.is_exist[i] = 0

    def full_search(self) -> None:
        num = 0

        for i in range(self.n):
            for j in range(self.n):
                cnt = 3
                nums: List[List[int]] = []
                y = i
                x = j
                num += self.a_list[y][x] * (10 ** 3)
                cnt -= 1




def main():
    n = int(input())
    a_list: List[List[int]] = []
    for _ in range(n):
        a_list.append(list(map(int, input().split())))
