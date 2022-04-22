





def main():
    h, w, a, b = map(int, input().split())
    
    
    codinate = [['0' for _ in range(w)] for _ in range(h)]
    for i in range(h):
        for j in range(w):
            x = i + 1
            y = j + 1
            
            if (x > b and y <= a) or (x <= b and y > a):
                codinate[i][j] = '1'
                
    for i in range(h):
        print(''.join(codinate[i]))
        
if __name__ == '__main__':
    main()
    