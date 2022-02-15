
class UnionFind():
    def __init__(self, n: int) -> None:
        self.parent_list = [-1 for _ in range(n)]
        self.size_list = [1 for _ in range(n)]
        
        
    def root(self, x: int) -> int:
        if self.parent_list[x] == -1:
            return x
        else:
            self.parent_list[x] = self.root(self.parent_list[x])
            return self.parent_list[x]


    def is_same(self, x: int, y: int) -> bool:
        return self.root(x) == self.root(y)


    def unite(self, x: int, y) -> bool:
        x = self.root(x)
        y = self.root(y)

        if x == y:
            return False

        if self.size_list[x] < self.size_list[y]:
            x, y = y, x

        self.parent_list[y] = x
        self.size_list[x] += self.size_list[y]
        return True


    def size(self, x: int) -> int:
        return self.size_list[self.root(x)]


    def count_root(self) -> int:
        cnt = 0
        for x in range(n):
            if self.root(x) == x:
                cnt += 1

        return cnt


if __name__ == '__main__':
    n, m = map(int, input().split())
    union = UnionFind(n)
    for _ in range(m):
        a, b = map(int, input().split())
        a -= 1
        b -= 1
        union.unite(a, b)

    ans = union.count_root() - 1
    print(ans)
