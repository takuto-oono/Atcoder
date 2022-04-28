





def change_string(num):
    st = str(num)
    if len(st) == 1:
        st = '00' + st
    
    if len(st) == 2:
        st = '0' + st
    
    return st

def create_S_states(S):
    s_state = [[] for _ in range(10)]
    for i in range(len(S)):
        x = int(S[i])
        s_state[x].append(i)

    return s_state

def search_S_states(m, list):
    for l in list:
        if l > m:
            return l
        
    return -1
    


def fullSearch(s_state):
    ans = 0
    for i in range(1000):
        x = change_string(i)
        m = -1
        for j in range(3):
            x_j = int(x[j])
            m = search_S_states(m, s_state[x_j])

            if m == -1:
                break
        
        if m == -1:
            continue
        
        ans += 1
    
    print(ans)














def main():
    n = int(input())
    S = input()
    s_state = create_S_states(S)
    fullSearch(s_state)

    




if __name__ == '__main__':
    main()

