a, b, x = map(int, input().split())
a_ans = a // x
b_ans = b // x
if a % x == 0:
    a_ans -= 1

ans = b_ans - a_ans
print(ans)


