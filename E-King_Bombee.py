from typing import Tuple, List

M = 998244353


class KingBombee:
    def __init__(self, n: int, m: int, k: int, s: int, t: int, x: int) -> None:
        self.n = n
        self.m = m
        self.k = k
        self.s = s - 1
        self.t = t - 1
        self.x = x - 1
        self.graph_list = [[] for _ in range(self.n)]
        self.create_graph_list()
        self.dp_list = [[0, 0] for _ in range(self.n)]
        self.init_dp_list()

    def create_graph_list(self) -> None:
        for _ in range(self.m):
            u, v = map(int, input().split())
            u -= 1
            v -= 1
            self.graph_list[u].append(v)
            self.graph_list[v].append(u)

    def init_dp_list(self) -> None:
        self.dp_list[self.s] = [1, 0]

    def update_dp_list(self) -> None:
        new_dp_list = [[0, 0] for _ in range(self.n)]
        for now_point in range(self.n):
            for next_point in self.graph_list[now_point]:
                if next_point == self.x:
                    new_dp_list[next_point][0] += self.dp_list[now_point][1]
                    new_dp_list[next_point][1] += self.dp_list[now_point][0]
                else:
                    new_dp_list[next_point][0] += self.dp_list[now_point][0]
                    new_dp_list[next_point][1] += self.dp_list[now_point][1]
                new_dp_list[next_point][0] %= M
                new_dp_list[next_point][1] %= M

        for i in range(self.n):
            for j in range(2):
                self.dp_list[i][j] = new_dp_list[i][j] % M

    def main_operate(self) -> int:
        for _ in range(self.k):
            self.update_dp_list()
        return self.dp_list[self.t][0]


def main():
    n, m, k, s, t, x = map(int, input().split())
    print(KingBombee(n, m, k, s, t, x).main_operate())


if __name__ == '__main__':
    main()
