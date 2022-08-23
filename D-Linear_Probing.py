class LinerProbing:
    def __init__(self) -> None:
        self.n = 2 ** 20
        self.q = int(input())
        self.a_list = [-1 for _ in range(self.n)]
        self.changing_index_list = [i for i in range(self.n)]

    def rewrite_a_list(self, index: int, value: int) -> None:
        self.a_list[index] = value
        self.changing_index_list[index] = self.changing_index_list[(index + 1) % self.n]

    def find_index(self, h: int) -> int:
        rewrite_index_list = []
        while self.changing_index_list[h] != h:
            rewrite_index_list.append(h)
            h = self.changing_index_list[h]
        for index in rewrite_index_list:
            self.changing_index_list[index] = h
        return h

    def process1(self, x: int) -> None:
        self.rewrite_a_list(self.find_index(x % self.n), x)

    def process2(self, x: int) -> None:
        print(self.a_list[x % self.n])

    def main_process(self):
        for _ in range(self.q):
            t, x = map(int, input().split())
            if t == 1:
                self.process1(x)
            if t == 2:
                self.process2(x)


def main():
    LinerProbing().main_process()


if __name__ == '__main__':
    main()
