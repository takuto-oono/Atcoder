from typing import List
condidate_1 = []
condidate_2 = []


def create_condidate_list(x: int, y: int) -> List:
    return [[x + 1, y + 2], [x + 2, y + 1], [x + 2, y - 1], [x + 1, y - 2], [x - 1, y - 2], [x - 2, y - 1], [x - 2, y + 1], [x - 1, y + 2]]


if __name__ == "__main__":
    x1, y1, x2, y2 = map(int, input().split())
    condidate_1 = create_condidate_list(x1, y1)
    condidate_2 = create_condidate_list(x2, y2)

    for c1 in condidate_1:
        for c2 in condidate_2:
            if c1 == c2:
                print('Yes')
                exit()

    print('No')
