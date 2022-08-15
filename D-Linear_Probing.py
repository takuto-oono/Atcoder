class LinerProbing:
    def __init__(self) -> None:
        self.n = 2 ** 20
        self.q = int(input())
        self.query_list = []
        for _ in range(self.q):
            self.query_list.append(tuple(map(int, input().split())))
        self.a_dic = {}
        self.a_dic_keys_list = [i for i in range(self.n)]

    def rewrite_a_list(self, index: int, value: int) -> None:
        self.a_dic[index] = value
        self.a_dic_keys_list[index] = self.a_dic_keys_list[(index + 1) % self.n]

    def find_index(self, h: int) -> int:
        while self.a_dic_keys_list[h] != h:
            h = self.a_dic_keys_list[h]
        return h

    def process1(self, x: int) -> None:
        h = x % self.n
        if h not in self.a_dic.keys():
            self.rewrite_a_list(h, x)
        else:
            self.rewrite_a_list(self.find_index(h), x)

    def process2(self, x: int) -> None:
        x %= self.n
        if x in self.a_dic.keys():
            print(self.a_dic[x])
        else:
            print(-1)

    def main_process(self):
        for (t, x) in self.query_list:
            if t == 1:
                self.process1(x)
            if t == 2:
                self.process2(x)


def main():
    LinerProbing().main_process()


if __name__ == '__main__':
    main()
