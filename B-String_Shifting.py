





def shift(string):
    begin = string[0]
    l = len(string)
    new_string = ''
    for i in range(l):
        if i == l - 1:
            new_string += string[0]
            continue
        new_string += string[i + 1]

    return new_string

def main():
    s = input()
    s_list = []
    
    
    for i in range(len(s)):
        s = shift(s)
        s_list.append(s)
    
    s_list.sort()
    print(s_list[0])
    print(s_list[len(s) - 1])

main()



