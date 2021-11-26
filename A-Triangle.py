





def main():
    s = int(input())
    coordinate_list = [0, 0, -1, 0, 0, -1]
    for i in range(1, 10 ** 9 + 1):
        
        if s % i == 0 and s // i <= 10 ** 9:
            coordinate_list[2] = i
            coordinate_list[5] = s // i
            break
    
    print(*coordinate_list)
    
if __name__ == '__main__':
    main()