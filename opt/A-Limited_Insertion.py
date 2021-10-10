n = int(input())
B = list(map(int, input().split()))

Ans_list = []
while(len(B) > 0):
    n = len(B)

    for i in reversed(range(len(B))):

        if B[i] == i + 1:
            Ans_list.append(i + 1)
            del B[i]
            break
    if n == len(B):
        print(-1)
        exit()

for i in reversed(range(len(Ans_list))):
    print(Ans_list[i])






