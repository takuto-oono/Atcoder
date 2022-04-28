





def search_t_100(t):
    Output = [0 for i in range(t + 100)]
    for i in range(100):
        x = (t + 100) * (i + 1) // 100
        Output[x - 1] = 1

    A = []
    for i in range(len(Output)):
        if Output[i] == 0:
            A.append(i + 1)
    return A

def print_answer(n, Target_list, t):
    if len(Target_list) >= n:
        ans = Target_list[n - 1]

    else:
        n_mod = n % len(Target_list)


        ans = Target_list[n_mod - 1]
        if n % len(Target_list) == 0:
            ans += (100 + t) * (n // len(Target_list) - 1)
        else:
            ans += (100 + t) * (n // len(Target_list))

    print(ans)

def main():
    t, n = map(int, input().split())
    Target_list = search_t_100(t)
    print_answer(n, Target_list, t)

main()



