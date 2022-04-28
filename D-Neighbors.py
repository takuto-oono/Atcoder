from typing import List

count_dic = {}


class UnionFind():
    def __init__(self, n: int) -> None:
        self.parent_list = [-1 for _ in range(n)]
        self.size_list = [1 for _ in range(n)]

    def root(self, x: int) -> int:
        if self.parent_list[x] == -1:
            return x

        self.parent_list[x] = self.root(self.parent_list[x])
        return self.parent_list[x]

    def is_same(self, x: int, y: int) -> bool:
        return self.root(x) == self.root(y)

    def unite(self, x: int, y: int) -> bool:
        x = self.root(x)
        y = self.root(y)

        if x == y:
            return False

        if self.size_list[x] < self.size_list[y]:
            x, y = y, x

        self.parent_list[y] = x
        self.size_list[x] += self.size_list[y]
        return True

    def create_root_list(self) -> List[int]:
        root_list = []
        for x in range(len(self.parent_list)):
            if self.parent_list[x] == -1:
                root_list.append(x)

        return root_list


def count(x: int) -> bool:
    if x in count_dic:
        count_dic[x] += 1
    else:
        count_dic[x] = 1

    if count_dic[x] > 2:
        return True

    else:
        return False


def check_number_of_appearances(ab_list: List) -> bool:
    for ab in ab_list:
        a = ab[0]
        b = ab[1]

        if count(a):
            return True

        if count(b):
            return True

    return False


if __name__ == '__main__':
    n, m = map(int, input().split())
    uf = UnionFind(n)
    ab_list = []
    for _ in range(m):
        a, b = map(int, input().split())
        a -= 1
        b -= 1
        if uf.unite(a, b) == False:
            print('No')
            exit()
        ab_list.append([a, b])

    if check_number_of_appearances(ab_list):
        print('No')
        exit()

    print('Yes')
