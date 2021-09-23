import math





def Full_search(X, Prime_numbers):
    ans = 10 ** 25
    for i in range(2 ** len(Prime_numbers)):
        bag = []
        for j in range(len(Prime_numbers)):
            if ((i >> j) & 1):
                bag.append(Prime_numbers[j])

        product_of_all_numbers = 1
        for j in bag:
            product_of_all_numbers *= j

        for j in X:
            if math.gcd(product_of_all_numbers, j) == 1:
                product_of_all_numbers = 10 ** 25
                break

        ans = min(ans, product_of_all_numbers)

    return ans


def main():
    n = int(input())
    X = list(map(int, input().split()))
    Prime_numbers = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47]
    print(Full_search(X, Prime_numbers))

main()


