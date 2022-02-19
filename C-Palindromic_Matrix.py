from typing import List
h = 0
w = 0
a_list = []
count_letter_list = [0 for _ in range(26)]
ans = 'Yes'


def change_int_from_char(c: str) -> int:
    return ord(c) - 97


def count_letter() -> None:
    for y in range(h):
        for x in range(w):
            count_letter_list[change_int_from_char(a_list[y][x])] += 1


def check_is_multiple_of_4(ans: str) -> str:
    for count in count_letter_list:
        if count % 4 != 0:
            ans = "No"
            
    return ans


def check_is_palindrome(memo_list: List[int], n: int) -> bool:
    odd_cnt = 0
    for memo in memo_list:
        if memo % 2 == 1:
            odd_cnt += 1

    if n % 2 == 0:
        if odd_cnt > 0:
            return False

    if n % 2 == 1:
        if odd_cnt > 1:
            return False

    return True


if __name__ == '__main__':
    h, w = map(int, input().split())
    ans = "Yes"
    for _ in range(h):
        a = list(input())
        a_list.append(a)

    count_letter()

    if h % 2 == 0 and w % 2 == 0:
        ans = check_is_multiple_of_4(ans)

    elif h % 2 == 0 and w % 2 == 1:
        memo_list = [0 for _ in range(26)]
        for i, count in enumerate(count_letter_list):
            if count % 4 != 0:
                m = count % 4
                memo_list[i] = m
                count_letter_list[i] -= m

        if sum(memo_list) > h:
            ans = "No"

        elif sum(memo_list) < h:
            if sum(memo_list) - h % 4 != 0:
                ans = "No"

            else:
                check_is_palindrome(memo_list, h)
        else:
            check_is_palindrome(memo_list, h)

    elif h % 2 == 1 and w % 2 == 0:
        memo_list = [0 for _ in range(26)]
        for i, count in enumerate(count_letter_list):
            if count % 4 != 0:
                m = count % 4
                memo_list[i] = m
                count_letter_list[i] -= m

        if sum(memo_list) > w:
            ans = "No"

        elif sum(memo_list) < w:
            if sum(memo_list) - w % 4 != 0:
                ans = "No"

            else:
                check_is_palindrome(memo_list, w)
        else:
            check_is_palindrome(memo_list, w)

    else:
        memo_list = [0 for _ in range(26)]
        for i, count in enumerate(count_letter_list):
            if count % 4 != 0:
                m = count % 4
                memo_list[i] = m
                count_letter_list[i] -= m

        cnt = 0
        for memo in memo_list:
            if memo == 1:
                cnt += 1

        if cnt != 1:
            ans = 'No'

        else:
            for memo in memo_list:
                if memo % 2 == 1:
                    ans = "No"
                    break

    print(ans)
