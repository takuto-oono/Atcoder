





def main():
    n = int(input())
    list_a = []
    for i in range(n):
        a = int(input())
        list_a.append(a)
    
    ans = 'second'
    for a in list_a:
        if a % 2 == 1:
            ans = 'first'
            break

    print(ans)
    
if __name__ == '__main__':
    main()

