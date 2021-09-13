import itertools





def main():
    S, k = input().split()
    n = len(S)
    k = int(k) - 1
    S = list(S)
    C = list(itertools.permutations(S, n))
    C = list(set(C))
    C.sort()
    ans = ''.join(C[k])
    print(ans)

main()
