





def main():
    n, m, k = map(int, input().split())
    friend_list = []
    for i in range(m):
        a, b = map(int, input().split())
        friend_list.append([a, b].sort())
    
    block_list = []
    for i in range(k):
        c, d = map(int, input().split())
        block_list.append([c, d].sort())
    
    k = 0
    new_block_list = [[] for _ in range(n)]
    
    for i in range(k):
        new_block_list[block_list[i][0] - 1].append(block_list[i][1])
        new_block_list[block_list[i][1] - 1].append(block_list[i][0])
    
    
        
            
            
        