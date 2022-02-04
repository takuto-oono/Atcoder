def main():
    n = int(input())
    t_list = []
    skill_list = []
    for i in range(n):
        l = list(map(int, input().split()))
        t = l.pop(0)
        t_list.append(t)
        skill_list.append(l)

    
    


if __name__ == '__main__':
    main()
