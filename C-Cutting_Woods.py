L, Q = map(int, input().split())
Cut_list = []


def process1(x: int) -> None:
    i = 0
    if len(Cut_list) == 0:
        Cut_list.append(x)
        return

    if len(Cut_list) == 1:
        if x < Cut_list[0]:
            Cut_list.insert(0, x)
        else:
            Cut_list.append(x)
        return

    while i < len(Cut_list) - 1:
        flag = (Cut_list[i] < x) and (Cut_list[i + 1] > x)
        if flag:
            break
    Cut_list.insert(i + 1, x)


def main():
    for _ in range(Q):
        c, x = map(int, input().split())
        if c == 1:
            process1(x)
        if c == 2:
            process2(x)