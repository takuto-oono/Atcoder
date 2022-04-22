from collections import deque

if __name__ == '__main__':
    s_string = input()
    
    t_deque = deque()
    
    reverse_switch = 1
    for s in s_string:
        if s == 'R':
            reverse_switch *= -1
            continue
        
        if reverse_switch == 1:
            if t_deque and t_deque[-1] == s:
                t_deque.pop()
                
            else:
                t_deque.append(s)
        
        else:
            if t_deque and t_deque[0] == s:
                t_deque.popleft()
            else:
                t_deque.appendleft(s)
    
    if reverse_switch == -1:
        t_deque = reversed(t_deque)
    
    print(''.join(t_deque))