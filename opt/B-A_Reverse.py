def reverse_string_r_l(left, right, s_string):
    s_list = list(s_string)
    left -= 1
    right -= 1
    while(True):
        if left >= right:
            return ''.join(s_list)

        s_list[left], s_list[right] = s_list[right], s_list[left]
        left += 1
        right -= 1


if __name__ == '__main__':
    l, r = map(int, input().split())
    s = input()
    print(reverse_string_r_l(l, r, s))
