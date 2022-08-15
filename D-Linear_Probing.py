class LinerProbing:
    def __init__(self) -> None:
        self.n = 2 ** 20
        self.q = int(input())
        self.query_list = []
        for _ in range(self.q):
            self.query_list.append(tuple(map(int, input().split())))
        self.a_dic = {}
        self.a_dic_keys_list = []

    def rewrite_a_list(self, index: int, value: int) -> None:
        self.a_dic[index] = value
        self.a_dic_keys_list.append(index)
        self.a_dic_keys_list.sort()

    def process1(self, x: int) -> None:
        h = x % self.n
        if h not in self.a_dic.keys():
            self.rewrite_a_list(h, x)
        else:
            new_h = self.a_dic_keys_list[-1] + 1
            is_search = False
            for i in range(len(self.a_dic_keys_list) - 1):
                if self.a_dic_keys_list[i] == h:
                    is_search = True
                if is_search:
                    if self.a_dic_keys_list[i + 1] > self.a_dic_keys_list[i] + 1:
                        new_h = self.a_dic_keys_list[i] + 1
                        break
            self.rewrite_a_list(new_h, x)

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
