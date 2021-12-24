





def cal1(cx, cy, h, x, y):
    return abs(cx - x) + abs(cy - y) + h

def cal2(cx, cy, h, x, y):
    return max(h - abs(cx - x) - abs(cy - y), 0)

def main():
    n = int(input())
    pyramid_information = []
    for i in range(n):
        x, y, h = map(int, input().split())
        pyramid_information.append([x, y, h])
    
    for cx in range(101):
        for cy in range(101):
            flag1 = True
            h = -1
            for i in range(n):
                if pyramid_information[i][2] == 0:
                    continue
                    
                if h == -1:
                    h = cal1(cx, cy, pyramid_information[i][2], pyramid_information[i][0], pyramid_information[i][1])
                    continue
                
                if h != cal1(cx, cy, pyramid_information[i][2], pyramid_information[i][0], pyramid_information[i][1]):
                    flag1 = False
                    break

            if flag1:
                flag2 = True
                for i in range(n):
                    if pyramid_information[i][2] != cal2(cx, cy, h, pyramid_information[i][0], pyramid_information[i][1]):
                        flag2 = False
                        break

                if flag2:
                    print(cx, cy, h)
                    exit()
                
                
            
                
if __name__ == '__main__':
    main()
    
                