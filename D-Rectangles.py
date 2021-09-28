import itertools





def Same_X(Coordinate):
    Coordinate.sort()
    Same_x = []
    i = 0
    while(i < len(Coordinate) - 1):
        same_x = [Coordinate[i][1]]
        x = Coordinate[i][0]

        for j in range(i + 1, len(Coordinate)):
            if x != Coordinate[j][0]:
                i += 1
                break

            same_x.append(Coordinate[j][1])
            i += 1


        if len(same_x) > 1:
            Same_x.append(same_x)

    return Same_x

def Create_full_list(Same_X):
    Full_list = []
    for same_x in Same_X:
        P = list(itertools.combinations(same_x, 2))
        for j in range(len(P)):
            Full_list.append(list(P[j]))

    Full_list.sort()
    return Full_list

def Find_combination(Full_list):
    ans = 0
    i = 0
    while(i < len(Full_list) - 2):
        c = 1
        for j in range(i + 1, len(Full_list)):
            x = Full_list[i]
            if x != Full_list[j]:
                i += 1
                break

            c += 1
            i += 1

        ans += c * (c - 1) // 2

    return ans




def main():
    n = int(input())
    Coordinate = []
    for i in range(n):
        x, y = map(int, input().split())
        Coordinate.append([x, y])

    Same_x = Same_X(Coordinate)
    Full_list = Create_full_list(Same_x)
    print(Find_combination(Full_list))

main()























