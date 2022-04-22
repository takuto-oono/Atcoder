





def Find_k(sum_A, A, x):
    ans = (x // sum_A) * len(A)
    remainder = x % sum_A

    for i in range(len(A)):
        if remainder < 0:
            return ans

        if i == len(A) - 1:
            return ans + 1

        ans += 1
        remainder -= A[i]



def main():
    n = int(input())
    A = list(map(int, input().split()))
    x = int(input())
    sum_A = sum(A)
    print(Find_k(sum_A, A, x))

main()



