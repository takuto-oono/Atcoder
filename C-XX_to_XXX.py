from typing import List


def create_string_list(str: str) -> List[List[str]]:
    s: List[str] = []
    string_list: List[List[str]] = []
    for i, t in enumerate(str):
        if i == len(str) - 1:
            if t == str[i - 1]:
                s.append(t)
            else:
                string_list.append(s)
                s = [t]
            string_list.append(s)
            break
        if i == 0:
            s.append(t)
            continue
        if t == str[i - 1]:
            s.append(t)
            continue
        if t != str[i - 1]:
            string_list.append(s)
            s = [t]
    return string_list


def judge(s: str, t: str) -> bool:
    s_list = create_string_list(s)
    t_list = create_string_list(t)
    if len(s_list) != len(t_list):
        return False
    for i in range(len(s_list)):
        if s_list[i] != t_list[i]:
            if len(s_list[i]) > len(t_list[i]):
                return False
            if len(s_list[i]) == 1 or len(t_list[i]) == 1:
                return False
            if s_list[i][0] != t_list[i][0]:
                return False

    return True


def main():
    if judge(input(), input()):
        print('Yes')
    else:
        print('No')


if __name__ == '__main__':
    main()
