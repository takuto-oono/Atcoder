def main(case):
    if case % 2 == 1:
        return "Odd"
    else:
        odd_count, even_count = 0, 0
        x = case
        for i in range(2, 10 ** 9 + 1):
            if i > x:
                break
            while(x % i == 0):
                x //= i
                if i % 2 == 0:
                    even_count += 1
                else:
                    odd_count += 1
        odd = 2 ** odd_count
        even = 2 ** (even_count + odd_count) - odd
        if even == odd:
            return "Same"
        elif even > odd:
            return "Even"
        elif odd > even:
            return "Odd"



t = int(input())
for i in range(t):
    case = int(input())
    print(main(case))
    