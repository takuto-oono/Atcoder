import itertools





def Create_same_x(Coordinate):
    Coordinate.sort()
    l = len(Coordinate)
    i = 0
    Same_x = []
    memo = []
    while(i < l - 1):
        for j in range(i + 1, l):
            if j == l - 1:
                if Coordinate[i][0] == Coordinate[j][0]:
                    if len(memo) == 0:
                        Same_x.append([Coordinate[i][1], Coordinate[j][1]])

                    else:
                        memo.append(Coordinate[j][1])
                        Same_x.append(memo)

                i = j
                break

            if j == i + 1:
                if Coordinate[i][0] != Coordinate[j][0]:
                    i += 1
                    break

                memo = [Coordinate[i][1], Coordinate[j][1]]

            else:
                if Coordinate[i][0] != Coordinate[j][0]:
                    Same_x.append(memo)
                    memo = []
                    i = j
                    break

                memo.append(Coordinate[j][1])

    return Same_x

def Combination(x):
    ans = x * (x - 1) // 2
    if ans > 0:
        return ans
    else:
        return 0

def Create_edge_list(Same_x):
    Edge = []
    l = len(Same_x)
    for i in range(l):
        for edge in itertools.combinations(Same_x[i], 2):
            Edge.append(list(edge))

    return Edge

def Find_rectangle(Edge):
    Edge.sort()
    l = len(Edge)
    i = 0
    ans = 0
    memo = 0
    while(i < l - 1):
        for j in range(i + 1, l):
            if j == l - 1:
                if Edge[i] == Edge[j]:
                    ans += Combination(memo + 1)

                else:
                    ans += Combination(memo)

                i = j
                break

            elif j == i + 1:
                if Edge[i] != Edge[j]:
                    i += 1
                    break

                memo = 2

            else:
                if Edge[i] != Edge[j]:
                    ans += Combination(memo)
                    memo = 0
                    i = j
                    break

                memo += 1

    return ans


def main():
    n = int(input())
    Coordinate = []
    for i in range(n):
        x, y = map(int, input().split())
        Coordinate.append([x, y])

    Same_x = Create_same_x(Coordinate)
    Edge = Create_edge_list(Same_x)
    print(Find_rectangle(Edge))





main()


