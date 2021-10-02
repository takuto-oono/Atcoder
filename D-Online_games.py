





def Entry(A, Online_people):
    A.sort()
    n = len(A)
    for i in range(n):
        Online_people[i] = 10 ** 100 - A[i]
    

    return Online_people

def Leaving(B, Online_people):
    B.sort(reverse=True)
    n = len(B)
    for i in range(n):
        
        b = 10 ** 100 - B[i]
        Online_people[i] = Online_people[i] - b
        
        
    
    return Online_people

def Create_ans(Online_people):
    Ans = list(reversed(Online_people))
    
    n = len(Online_people)
    c = 0
    for i in range(n):
        Ans[i] = Ans[i] - c
        c += Ans[i]
    
    Ans = list(reversed(Ans))
    for i in range(n):
        Ans[i] = str(Ans[i])

    print(' '.join(Ans))
        

def main():
    n = int(input())
    A = []
    B = []
    for i in range(n):
        a, b = map(int, input().split())
        A.append(a)
        B.append(a + b)
    
    Online_people = [0 for _ in range(n)]
    
    Online_people = Entry(A, Online_people)

    Online_people = Leaving(B, Online_people)

    Create_ans(Online_people)


main()

