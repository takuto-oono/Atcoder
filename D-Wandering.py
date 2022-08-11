from typing import List, Generator


def create_cumulative_sum_list(nums: List[int]) -> Generator[int, None, None]:
    result = 0
    for num in nums:
        result += num
        yield result


def find_max_coordinate(a_list: List[int], n: int) -> int:
    destination_list = [0 for _ in range(n)]
    max_coordinate_list = [0 for _ in range(n)]
    cumulative_sum_list = [cumulative_sum for cumulative_sum in create_cumulative_sum_list(a_list)]
    max_cumulative_sum = cumulative_sum_list[0]
    for i in range(n):
        max_cumulative_sum = max(max_cumulative_sum, cumulative_sum_list[i])
        if i == 0:
            max_coordinate_list[0] = max(max_cumulative_sum, 0)
            destination_list[0] = max_cumulative_sum
            continue
        max_coordinate_list[i] = destination_list[i - 1] + max_cumulative_sum
        destination_list[i] = destination_list[i - 1] + cumulative_sum_list[i]
    return max(max_coordinate_list)


def main():
    n = int(input())
    a_list = list(map(int, input().split()))
    print(find_max_coordinate(a_list, n))


if __name__ == '__main__':
    main()
