from typing import List, Tuple


class Circumferences:
    def __init__(self, n: int, sx: int, sy: int, tx: int, ty: int, circles: List[Tuple[int, int, int]]) -> None:
        self.n = n
        self.s = (sx, sy)
        self.t = (tx, ty)
        self.circles = circles

    def create_graphs(self) -> List[List[int]]:
        graphs = [[] for _ in range(self.n)]

        for i in range(self.n):
            for j in range(i + 1, self.n):
                circle_i = self.circles[i]
                circle_j = self.circles[j]
                if (circle_i[2] + circle_j[2]) ** 2 < (circle_i[0] - circle_j[0]) ** 2 + (
                        circle_i[1] - circle_j[1]) ** 2:
                    continue
                if (circle_i[2] - circle_j[2]) ** 2 > (circle_i[0] - circle_j[0]) ** 2 + (
                        circle_i[1] - circle_j[1]) ** 2:
                    continue
                graphs[i].append(j)

        return graphs

    def is_circle_on_the_point(self, x: int, y: int, circle_num: int) -> bool:
        circle = self.circles[circle_num]
        if circle[2] ** 2 == (x - circle[0]) ** 2 + (y - circle[1]) ** 2:
            return True
        return False

    def find_circle_on_the_point(self, point: Tuple[int, int]) -> int:
        for circle_num in range(self.n):
            if self.is_circle_on_the_point(point[0], point[1], circle_num):
                return circle_num


class UnionFind:
    def __init__(self, n: int) -> None:
        self.n = n
        self.parents = [-1] * n

    def find(self, x: int) -> int:
        if self.parents[x] < 0:
            return x
        self.parents[x] = self.find(self.parents[x])
        return self.parents[x]

    def union(self, x: int, y: int) -> None:
        x = self.find(x)
        y = self.find(y)

        if x == y:
            return

        if self.parents[x] > self.parents[y]:
            x, y = y, x

        self.parents[x] += self.parents[y]
        self.parents[y] = x

    def size(self, x: int) -> int:
        return -self.parents[self.find(x)]

    def same(self, x: int, y: int) -> bool:
        return self.find(x) == self.find(y)


def main_judge(n: int, sx: int, sy: int, tx: int, ty: int, circles: List[Tuple[int, int, int]]) -> bool:
    circumferences = Circumferences(n, sx, sy, tx, ty, circles)
    graphs = circumferences.create_graphs()
    union = UnionFind(n)
    for i, circle_list in enumerate(graphs):
        for circle_num in circle_list:
            union.union(i, circle_num)

    if union.same(circumferences.find_circle_on_the_point((sx, sy)), circumferences.find_circle_on_the_point((tx, ty))):
        return True
    return False


def main():
    n = int(input())
    sx, sy, tx, ty = map(int, input().split())
    circles = []
    for _ in range(n):
        x, y, r = map(int, input().split())
        circles.append((x, y, r))
    if main_judge(n, sx, sy, tx, ty, circles):
        print('Yes')
    else:
        print('No')


if __name__ == '__main__':
    main()
