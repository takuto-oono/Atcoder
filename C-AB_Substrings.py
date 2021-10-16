





def classification_string(s):
    if s[0] == 'B' and s[-1] == 'A':
        return 0
    
    if s[0] == 'B':
        return 2
    
    if s[-1] == 'A':
        return 1
    
    return -1

def create_generation_count(classification_result):
    generation_count = 0
    ab = classification_result[0]
    a = classification_result[1]
    b = classification_result[2]

    if ab > 0:
        generation_count += ab - 1
        if a > 0:
            generation_count += 1
            a -= 1
        
        if b > 0:
            generation_count += 1
            b -= 1
        
        generation_count += min(a, b)
        return generation_count
    
    if ab == 0:
        generation_count += min(a, b)
        return generation_count
    


def main():
    n = int(input())
    S = []
    for i in range(n):
        s = input()
        S.append(s)
    
    ans = 0
    classification_result = [0, 0, 0]

    for i in range(n):
        s = S[i]
        for j in range(len(s) - 1):
            if s[j] == 'A' and s[j + 1] == 'B':
                ans += 1
        
        result = classification_string(s)
        if result >= 0:
            classification_result[result] += 1
    
    ans += create_generation_count(classification_result)
    print(ans)
    
        

    
    
    
        


main()
