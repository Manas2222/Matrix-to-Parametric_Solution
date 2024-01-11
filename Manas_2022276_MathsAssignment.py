def printMat(lst):
    for i in range (len(lst)):
        for j in range (len(lst[i])):
            print(lst[i][j],end= " ")
        print()


def rowDivideOperation(lst,row,counter,k):
    for i in range (counter,len(lst[0])):
        lst[row][i] /= k
    return lst


def rowOperation(lst,row1,row2,k):
    for i in range (len(lst[row2])):
        lst[row2][i] = lst[row2][i] - (lst[row1][i]*k)
    return lst



def rowExchange (lst,row1,row2):
    lst[row1],lst[row2]= lst[row2],lst[row1]
    return lst


def findFreeVars(lst):
    temp = []
    counter1 = 0
    counter2 = 0
    while counter1 < len(lst) and counter2 < len(lst[0]):
        if lst[counter1][counter2] != 1:
            temp.append(counter2)
            counter2+=1
            continue
        if lst[counter1][counter2] == 1:
            counter1+=1
            counter2+=1
            continue
    while counter2 < len(lst[0]):
        temp.append(counter2)
        counter2+=1
    return temp


def findBasicVars(lst,temp):
    basicVars = []
    for i in range (len(lst[0])):
        if i not in temp:
            basicVars.append(i)
    return basicVars


def makeItRREF(lst):
    counter1 = 0
    counter2 = 0
    while counter1 < len(lst) and counter2 < len(lst[0]):
        if lst[counter1][counter2] == 1:
            for i in range (0,counter1):
                lst = rowOperation(lst,counter1,i,lst[i][counter2])
            
            counter1+=1
            counter2+=1
            continue
        else:
            counter2+=1
            continue
    return lst


def parametricMatrix(lst,temp,basicVars):

    d = {}
    for i in range (len(basicVars)):
        di = {}
        for j in range (len(lst[i])):
            if j in temp:
                if lst[i][j] != 0:
                    di[j] = -lst[i][j]
                else:
                    di[j] = 0
        d[basicVars[i]] = di
    
    answer = []
    for i in range (len(temp)):
        l = [0]*len(lst[0])
        l[temp[i]] = 1

        for k,v in d.items():
            for k_,v_ in v.items():
                if k_ == temp[i]:
                    l[k] = v_
        
        answer.append(l)
    return answer


# 
row = int(input())
col = int(input())
lst = []
for i in range (row):
    c = input()
    c = [float(c.split(' ')[i]) for i in range (col)]
    lst.append(c)



counter1 = 0
counter2 = 0
while counter1 < row and counter2 < col:
    if lst[counter1][counter2] == 0:
        for i in range (counter1+1,row):
            if lst[i][counter2] != 0:
                lst = rowExchange(lst,counter1,i)
    if lst[counter1][counter2] == 0:
        counter2+=1
        continue
    
    if lst[counter1][counter2] != 0:
        lst = rowDivideOperation(lst,counter1,counter2,lst[counter1][counter2])
        for i in range (counter1+1,row):
            lst = rowOperation(lst,counter1,i,lst[i][counter2])
        counter1+=1
        counter2+=1

# Achieved REF

# printMat(lst)



lst = makeItRREF(lst)
print("RREF : ")
printMat(lst)

temp = findFreeVars(lst)
basicVars = findBasicVars(lst,temp)
# print(basicVars)
# print(temp)

answer = parametricMatrix(lst,temp,basicVars)
# print(f'answer is : \n{answer}')

for i in range (len(temp)):
    for j in range (row):
        answer[i][j] = round(answer[i][j],7)
# print(answer)

print("SOLUTION : ")
if len(temp) == 0 or len(temp) == col:
    l = [0]*col
    print("Trivial Solution")
    print(f'x = {l}')
else:
    for i in range (len(temp)):
        if i != len(temp)-1:
            print(f'x_{temp[i]+1} * {answer[i]} +',end = ' ')
        else:
            print(f'x_{temp[i]+1} * {answer[i]}')


