




 
def game(player1, player2, A, i):
    hand1 = A[player1][i]
    hand2 = A[player2][i]
    if hand1 == hand2:
        return -1
    
    if hand1 == 'G':
        if hand2 == 'P':
            return player2
        
    if hand1 == 'P':
        if hand2 == 'C':
            return player2
    
    if hand1 == 'C':
        if hand2 == 'G':
            return player2
    
    return player1

def print_ans(win_counter):
    for i in range(len(win_counter)):
        print(win_counter[i][1] + 1)

def main():
    n, m = map(int, input().split())
    A = []
    for i in range(2 * n):
        a = list(input())
        A.append(a)
    
        
    win_counter = [[m, i] for i in range(2 * n)]

    for i in range(m):
        for j in range(n):
            player1 = win_counter[2 * j][1]
            player2 = win_counter[2 * j + 1][1]
            jugement = game(player1, player2, A, i)

            if jugement == -1:
                continue

            for k in range(2 * n):
                if win_counter[k][1] == jugement:
                    win_counter[k][0] -= 1
                    break
            
            
        
        win_counter.sort()
    
    print_ans(win_counter)

            


                

main()
