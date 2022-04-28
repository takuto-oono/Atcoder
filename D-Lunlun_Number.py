





def generate_condidate(condidate, condidate_list, i):
    x = condidate[-1]
    condidate_list_i = condidate_list[i]
    
    if x == '0':
        condidate_1 = condidate + '0'
        condidate_2 = condidate + '1'
        condidate_list_i.append(condidate_1)
        condidate_list_i.append(condidate_2)
        return
    
    if x == '9':
        condidate_1 = condidate + '9'
        condidate_2 = condidate + '8'
        condidate_list_i.append(condidate_1)
        condidate_list_i.append(condidate_2)
        
        return
    
    if int(x) >= 1 and int(x) <= 8:
        condidate_1 = condidate + x
        condidate_2 = condidate + str(int(x) + 1)
        condidate_3 = condidate + str(int(x) - 1)
        condidate_list_i.append(condidate_1)
        condidate_list_i.append(condidate_2)
        condidate_list_i.append(condidate_3)
        return

def main():
    k = int(input())
    condidate_list = [[str(i + 1) for i in range(9)]]
    i = 1
    while(i <= 11):
        condidate_list.append([])
        for j in range(len(condidate_list[i - 1])):
            condidate = condidate_list[i - 1][j]
            generate_condidate(condidate, condidate_list, i)
        
        i += 1
    
    lunlun_list = []
    for i in range(len(condidate_list)):
        for j in range(len(condidate_list[i])):
            lunlun_list.append(int(condidate_list[i][j]))
    
    lunlun_list.sort()
    
    print(lunlun_list[k - 1])
    
if __name__ == '__main__':
    main()
    