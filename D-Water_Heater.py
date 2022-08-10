from typing import List


def is_supply_water(supply: int, demand: int) -> bool:
    if supply < demand:
        return False
    return True


def is_meet_the_demands(person_list: List[List[int]], w: int) -> bool:
    rising_demands = sorted([[person[0], person[2]] for person in person_list])
    decrease_in_demands = sorted([[person[1], person[2]] for person in person_list])
    r_index = 0
    d_index = 0
    now_demand = 0
    l = len(rising_demands)
    for t in range(2 * 10 ** 5 + 1):
        while r_index < l:
            if rising_demands[r_index][0] != t:
                break
            now_demand += rising_demands[r_index][1]
            r_index += 1
        while d_index < l:
            if decrease_in_demands[d_index][0] != t:
                break
            now_demand -= decrease_in_demands[d_index][1]
            d_index += 1

        if not is_supply_water(w, now_demand):
            return False

    return True


def main():
    n, w = map(int, input().split())
    person_list = []
    for _ in range(n):
        person_i = list(map(int, input().split()))
        person_list.append(person_i)

    if is_meet_the_demands(person_list, w):
        print('Yes')
    else:
        print('No')


if __name__ == '__main__':
    main()
