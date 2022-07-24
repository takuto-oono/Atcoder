class ChangingJewels:
    def __init__(self, n: int, x: int, y: int) -> None:
        self.x = x
        self.y = y
        self.red_cnt = [0 for _ in range(10)]
        self.blue_cnt = [0 for _ in range(10)]
        self.red_cnt[n - 1] = 1

        self.do_all_operate()
        self.print_blue_1()

    def operate_1(self) -> bool:
        for i in range(10):
            j = 10 - 1 - i
            if self.red_cnt[j] > 0 and j > 0:
                self.red_cnt[j - 1] += self.red_cnt[j]
                self.blue_cnt[j] += self.red_cnt[j] * self.x
                self.red_cnt[j] = 0
                return True
        return False

    def operate_2(self) -> bool:
        for i in range(10):
            j = 10 - 1 - i
            if self.blue_cnt[j] > 0 and j > 0:
                self.blue_cnt[j - 1] += self.blue_cnt[j] * self.y
                self.red_cnt[j - 1] += self.blue_cnt[j]
                self.blue_cnt[j] = 0
                return True
        return False

    def do_all_operate(self) -> None:
        while True:
            if self.operate_1() or self.operate_2():
                continue
            break

    def print_blue_1(self) -> None:
        print(self.blue_cnt[0])


def main():
    n, x, y = map(int, input().split())
    ChangingJewels(n, x, y)


if __name__ == '__main__':
    main()
