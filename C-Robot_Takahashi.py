from typing import List, Generator


def create_adult_list(w_list: List[int], s_list: List[str]) -> Generator[int, None, None]:
    for i, s in enumerate(s_list):
        if s == '1':
            yield w_list[i]


def create_child_list(w_list: List[int], s_list: List[str]) -> Generator[int, None, None]:
    for i, s in enumerate(s_list):
        if s == '0':
            yield w_list[i]


def cnt_ok_children(child_list: List[int], x: int) -> int:
    import bisect
    return bisect.bisect_left(child_list, x)


def full_search(w_list: List[int], s_list: List[str]) -> int:
    ans = 0
    child_list = sorted([w for w in create_child_list(w_list, s_list)])
    adult_list = sorted([w for w in create_adult_list(w_list, s_list)])
    cnt_adult = len(adult_list)
    cnt_child = len(child_list)

    if cnt_child == 0:
        return cnt_adult
    if cnt_adult == 0:
        return cnt_child

    for i, adult_weight in enumerate(adult_list):
        ans = max(cnt_adult - i + cnt_ok_children(child_list, adult_weight), ans)
    return ans


def main():
    _ = int(input())
    s_list = list(input())
    w_list = list(map(int, input().split()))
    print(full_search(w_list, s_list))


if __name__ == '__main__':
    main()
