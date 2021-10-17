





def determine_color(C, h, w, A):
    k = 0
    for i in range(h):
        if i % 2 == 0:
            for j in range(w):
                C[i][j] = k + 1
                A[k] -= 1
                if A[k] <= 0:
                    k += 1
            
            continue

        if i % 2 == 1:
            for j in range(w):
                C[i][w - j - 1] = k + 1
                A[k] -= 1
                if A[k] <= 0:
                    k += 1
            
            continue

    return C

def print_answer(C, h):
    for i in range(h):
        c = C[i]
        print(*c)

def main():
    h, w = map(int, input().split())
    n = int(input())
    A = list(map(int, input().split()))
    C = [[0 for _ in range(w)] for _ in range(h)]
    C = determine_color(C, h, w, A)
    print_answer(C, h)

main()