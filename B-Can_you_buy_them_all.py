def input1():
    n, x = map(int, input().split())
    A = list(map(int, input().split()))
    return n, x, A

def sort_list(A):
    for i in range(len(A)):
        if i % 2 == 1:
            A[i] = A[i] - 1

    A.sort()

def juge(n, x, A):
    c = 0
    for i in range(n):
        if x >= A[i]:
            c += 1
            x -= A[i]
        else:
            break

    if n == c:
        ans = 'Yes'
    else:
        ans = 'No'

    print(ans)


def main():
    n, x, A = input1()
    sort_list(A)
    juge(n, x, A)

main()



