def main():
    s1, s2, s3 = input().split()
    t1, t2, t3 = input().split()
    cnt = 0
    if s1 != t1:
        cnt += 1
    if s2 != t2:
        cnt += 1
    if s3 != t3:
        cnt += 1
    if cnt == 0:
        print('Yes')
    elif cnt == 2:
        print('No')
    elif cnt == 3:
        print('Yes')
    else:
        print('No')


if __name__ == '__main__':
    main()
