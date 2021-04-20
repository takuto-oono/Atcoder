n, m = map(int, input().split())
ans = 0
z = 10 ** 9 + 7
way_of_arrangement_monke = 1
way_of_arrangement_dog = 1
if n == m:
    for i in range(1, n + 1):
        way_of_arrangement_dog *= i
        if way_of_arrangement_dog >= z:
            way_of_arrangement_dog %= z

    for i in range(1, m + 1):
        way_of_arrangement_monke *= i
        if way_of_arrangement_monke >= z:
            way_of_arrangement_monke %= z

    ans = way_of_arrangement_monke * way_of_arrangement_dog * 2 % z

elif abs(n - m) == 1:
    for i in range(1, n + 1):
        way_of_arrangement_dog *= i
        if way_of_arrangement_dog >= z:
            way_of_arrangement_dog %= z

    for i in range(1, m + 1):
        way_of_arrangement_monke *= i
        if way_of_arrangement_monke >= z:
            way_of_arrangement_monke %= z

    ans = way_of_arrangement_monke * way_of_arrangement_dog % z

print(ans)



