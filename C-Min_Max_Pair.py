from typing import Tuple, Generator


def count_is_same_index_and_num(nums: Tuple[int]) -> int:
    result = 0
    for i, num in enumerate(nums):
        if i + 1 == num:
            result += 1
    return result


def create_list_index_and_num_pair(nums: Tuple[int]) -> Generator[Tuple[int, int], None, None]:
    for i, num in enumerate(nums):
        if i + 1 != num:
            result = (i + 1, num)
            yield tuple(sorted(result))


def count_is_not_same_index_and_num_pair(nums: Tuple[int]):
    index_and_num_pair_list = [t for t in create_list_index_and_num_pair(nums)]
    return len(index_and_num_pair_list) - len(set(index_and_num_pair_list))


def count_is_conditions(nums: Tuple[int]):
    same_index_and_num_counter = count_is_same_index_and_num(nums)
    return same_index_and_num_counter * (same_index_and_num_counter - 1) // 2 + count_is_not_same_index_and_num_pair(
        nums)


def main():
    _ = int(input())
    nums = tuple(map(int, input().split()))
    print(count_is_conditions(nums))


if __name__ == '__main__':
    main()
