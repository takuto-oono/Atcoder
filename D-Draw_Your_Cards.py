class DrawYourCards:
    def __init__(self):
        self.n, self.k = map(int, input().split())
        self.p_list = list(map(int, input().split()))
        self.operate_p_list()
        self.card_list = [-1 for _ in range(self.n)]

    def operate_p_list(self):
        for i in range(len(self.p_list)):
            self.p_list[i] -= 1

    def game(self):
        from bisect import bisect_left
        board = []
        union = UnionFind(self.n)

        for i, p in enumerate(self.p_list):
            if len(board) == 0:
                board.append(p)
                continue
            if p > board[-1]:
                board.append(p)
                continue
            index = bisect_left(board, p)
            union.union(p, board[index])
            if union.size(p) == self.k:






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

    def is_same(self, x: int, y: int) -> bool:
        return self.find(x) == self.find(y)

def main():
