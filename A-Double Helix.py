b = input()
ans = 0
def main(b):
    if b == 'A':
        ans = 'T'
    elif b == 'T':
        ans = 'A'
    elif b == 'G':
        ans = 'C'
    else:
        ans = 'G'
    return ans

print(main(b))
