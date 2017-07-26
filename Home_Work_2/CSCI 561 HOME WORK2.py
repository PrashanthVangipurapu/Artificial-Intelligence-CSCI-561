global matrixRel
matrixRel=[]

count=0
totalclause=[]
new=[]


def main():
    global clausecount
    clausecount=0
    #print "read input here"
    inputread()

def inputread():


    path="input1.txt"
    global input  #This will become global variable
    with open(path) as file:
         input = [[str(digit) for digit in line.split()] for line in file]
    print "input is "+str(input)
    guestnum=input[0][0]
    guestnum=int(guestnum)
    for i in range (0,guestnum):
       matrixRel.append([])
       for j in range (0,guestnum):
          matrixRel[i].append(0)
    print input
    #print "relation matrix is "
    #print matrixRel
    #print str(len(input))
    #print matrixRel
    jcount=0
    for i in range(1,len(input)):
         jcount=0
         friend1=input[i][jcount]
      #   print "friend 1 "+friend1+" "+str(i)
         friend1=int(friend1)
         friend1=friend1-1
         jcount=jcount+1
         friend2=int(input[i][jcount])
         friend2=int(friend2)
         friend2=friend2-1
         jcount=jcount+1
         rel=input[i][jcount]
         if rel== 'E':
            matrixRel[friend1][friend2]=-1
         elif rel=='F':
             matrixRel[friend1][friend2]=1
    #print "mat is "+str(matrixRel)

def createClause1():

    print "This is for all the guests "
    print input
    numguest=input[0][0]
    numguest=int(numguest)
    numtable=input[0][1]
    numtable=int(numtable)
    print "number of guests are "+str(numguest)
    print "number of tables are "+str(numtable)
    for i in range (1,numguest+1):
        totalclause.append([])
        for j in range (1,numtable+1):
            stri='x'+str(i)+str(j)
            totalclause[len(totalclause)-1].append(stri)
        totalclause.append([])
        for j in range(1,numtable+1):
            stri='~x'+str(i)+str(j)
            totalclause[len(totalclause) - 1].append(stri)


    print "totalclause is "+str(totalclause)




def createClause2():
    #print "input here is "+str(input)
    #print "length of input is "+str(len(input))
    #print "input[1] is "+str(input[1][2])
    for i in range(1,len(input)):
        print "input[i] is "+str(input[i])
     #   print "i is "+str(i)
        if input[i][2]=='F':
            guests=input[0][0]
            guests=int(guests)
            tables=input[0][1]
            tables=int (tables)
            first=input[i][0]
            second=input[i][1]
            #print "here "+str(clause2[0])
            flag=0
            for i in range (0,tables):
               if flag==0:
                 totalclause.append([])
                 stri1="~"+"x"+str(first)+str(i+1)
                 totalclause[len(totalclause)-1].append(stri1)
                 stri2="x"+str(second)+str(i+1)
                 totalclause[len(totalclause)-1].append(stri2)
                 flag=1                 #
               if flag==1:
                    totalclause.append([])
                    stri1="x"+str(first)+str(i+1)
                    totalclause[len(totalclause) - 1].append(stri1)
                    stri2="~"+"x"+str(second)+str(i+1)
                    totalclause[len(totalclause) - 1].append(stri2)
                    flag=0

def createClause3():
    #print "input is "
    #print input
    for i in range(1,len(input)):
        if input[i][2]=='E':
            guests = input[0][0]
            guests = int(guests)
            tables = input[0][1]
            tables = int(tables)
            first = input[i][0]
            second = input[i][1]
            for i in range(0,tables):
                totalclause.append([])
                stri1 = "~" + "x" + str(first) + str(i + 1)
                totalclause[len(totalclause) - 1].append(stri1)
                stri2 = '~'+"x" + str(second) + str(i + 1)
                totalclause[len(totalclause) - 1].append(stri2)

def PlResolution():
    print "length of totalclause is "+str(len(totalclause))

    while(1):
        i=0
        while(i<len(totalclause)):
          j=i+1
          while j<len(totalclause): #in range(i+1,len(totalclause)):
             print "the value of i in while loop "+str(i)
             print "The value of j here in while loop is "+str(j)
             print "totalclause of i is "+str(totalclause[i])
             print " and totalclause of j is " + str(totalclause[j])
             findres=get(totalclause[i],totalclause[j]) #if we can add then 1 else 0
             print "The value of findres is "+str(findres)
             print "j is "+str(j)
             if findres==1:
                 print "In findres about to add clause"
                 newtotal()
                 #i=i+1
                 if j==len(totalclause)-1:
                     print "all of j are completed for given i"
                     if i==len(totalclause)-1:
                         print "you are done exploring"
                         return
                     else:
                        i=i+1
                 else:
                     j=j+1
             elif findres==2:
                 print "NO"
                 return
             else:
                 if j ==len(totalclause)-1:
                     print "all of j are completed for a given i"
                     if i==len(totalclause)-1:
                         #print "global count is "+str(count)
                         print "you are done exploring"
                         print "totalclause is "+str(totalclause)
                         return
                     else:
                        i=i+1
                 else:
                     j=j+1
                     print "fuck code "+str(len(totalclause))
#Thus function is used to add a clause into totalclause.
def newtotal():
    count=0 #this variable traverses whole for loop and checks for duplicates
    for a in range (0,len(new)):
        if new[a] in totalclause:
            print "duplicate found while adding new total"
            continue
        else:
            addclause(new[a])
    print totalclause[len(totalclause)-1]


def addclause(list):  #call to this function will occur only when we checked that we can add our clause.
    global clausecount
    clausecount =clausecount+1
    totalclause.append([])
    length=len(list)
    for i in range(0,length):
        totalclause[len(totalclause)-1].append(list[i])
    print "global count is "+str(clausecount)



def get(str1,str2):   #Given two clauses str1 and str2, It will check whether we can make a new clause out of it.
    len1=len(str1)
    len2=len(str2)
    print "given two clauses are "
    print str1
    print str2
    print "length of str1 is "+str(len1)
    print "length of str2 is " + str(len2)
    for i in range (0,len1):
        first=str1[i]
        for j in range (0,len2):
            print "j is "+str(j)
            second=str2[j]
            negateres=negatecompare(first,second) #this will check whether the two clauses can be negated or not
            if negateres==0:  #0 indicates we cannot do negation for these two clauses so move on to next literal
                print "didn't found a result continue again"
                if j==len2-1:
                    print "all right clauses are done"
                    return 0
                else:
                    print "right clauses still there"
                    continue #check it once.
            else:
                if negateres==1:
                    if len1==1 and len2==1:
                        print "an empty clause is formed"
                        return 2
                    else:
                        print "yes there is a clause here"
                        supplyclause(str1,str2,i,j) #solution there so we nned to create a new clause and add it to new
                        return 1
def negatecompare(first,second):
    if len(first)==len(second):
        return 0
    else:
        if len(first)>len(second):
            if first=='~'+second:
                return 1
            else:
                return 0
        elif len(first)<len(second):
            if '~'+first==second:
                return 1
            else:
                return 0



def supplyclause(str1,str2,i,j):  #This function is used to create a new clause if there exists a soln for the given two source and target clauses
    print "str1 is "+str(str1)
    print "str1 is " + str(str2)
    print "i is "+str(i)
    print "j is "+str(j)
    #str1 is first set
    #str2 is second set
    #i represents the literal in i which matched with str2's literal
    #j represents the literal in j which matched with str1's literal
    new.append([])
    for a in range (0,len(str1)):
        if a==i:
            continue
        else:
          new[len(new)-1].append(str1[a])

    for b in range (0,len(str2)):
        if b==j:
            continue
        else:
            new[len(new)-1].append(str2[b])
    #print "new in supply clause is "+str(new)



def walksat():
    model=[]
    guest=input[0][0]
    guest=int(guest)
    table=input[0][1]
    table=int(table)
    model=getModel(model)
    print "model is "+str(model)
    while(1):
        result=modelsatisfy(model) #1
        if result==1:
            print "came here to return model"
            return model
        else:
            clause=selectrandomclause()  #2
            p=randomprobability() #3

            if p<0.5:
                #print "probability is less than 0.5"
                literal=randomliteralselect(clause) #4
                model=flipvalue(model,literal) #5
            else:
                if p>0.5:
                 import copy
                 print "unsatisfied clauses are"+str(unsatisfy)
                 print "len of unsatisfy is "+str(len(unsatisfy))
                 print "probability is greater than 0.5"
                 length=len(clause)
                 maxliteral = {}
                 for i in range(0,length):
                     print "clause[i] is "+str(clause[i])
                     value = findvalue(model, clause[i])
                     print "at p>0.5  a "+str(i)+" value is "+str(value)
                     satlen=getmaxflipliteral(copy.deepcopy(model),clause[i])
                     print "clause[i] is " + str(clause[i])
                     value = findvalue(model, clause[i])
                     print "at p>0.5  b  " + str(i) + " value is " + str(value)
                     if satlen==-1:
                         print "END"
                         return model
                     maxliteral[i]=satlen



                 print "maxliteral is "+str(maxliteral)
                 index=max(maxliteral, key=maxliteral.get)
                 print "index selected is "+str(index)
                 literal=clause[index]
                 print "selected literal is "+str(literal)
                 print "value check here is "+str(findvalue(model, literal))
                 model=flipvalue(model,literal)
                 print "value check here is 2 " + str(findvalue(model, literal))


    return model

def getModel(model):
    guest = input[0][0]
    guest = int(guest)
    table = input[0][1]
    table = int(table)
    for i in range (0,guest):
           model.append([])
           for j in range (0,table):
              model[i].append(0)
    import random
    for i in range(0,guest):
        index = random.randint(0, len(model[i]) - 1)
        model[i][index]=1
    return model

#1
def modelsatisfy(modeltest):
    global unsatisfy
    global satisfy
    unsatisfy=[]
    satisfy=[]
    count=0
    print "model is "+str(modeltest)
    print "len of totalclause is "+str(len(totalclause))
    for i in range(0,len(totalclause)):
        print "clause "+str(i)+" is "+str(totalclause[i])
        clause=totalclause[i]
        length=len(clause)
        print "length of clause is "+str(length)
        player=0
        flag=0
        for j in range(0,length): #This loop is used for getting the player and table
            flag = 0# this will become 1 as soon as we encounter a 1.
            literal=clause[j]
            lenliteral=len(literal)
            if '~' not in literal:   #lenliteral==3:
                print "our literal is of length 3"
                player=literal[1]
                player=int(player)-1
                table=literal[2]
                table=int(table)-1
                value = modeltest[player][table]
            else:
                print "our literal is of length 4"
                if '~' in literal: #  lenliteral==4:
                    player=literal[2]
                    player=int(player)-1
                    table=literal[3]
                    table=int(table)-1
                    value1 = modeltest[player][table]
                    if value1==0:
                        value=1
                    elif value1==1:
                        value=0

            print "player is "+str(player)+" "+" and table is "+str(table)

            print "value is "+str(value)
            if value==1:
                print "found a literal inside a clause with value 1"
                flag=1
                #satisfy.append([])
                satisfy.append(totalclause[i])
                print "satisfy set is "+str(satisfy)
                print "yes it is 1"
                break

        if flag==0:
            print "didnt found any 1 for this clause"
            unsatisfy.append(totalclause[i])
            print "unsatisfy set is "+str(unsatisfy)
    print "count is "+str(count)
    print "i is "+str(i)
    print "length of unsatisfy is "+str(len(unsatisfy))
    if len(unsatisfy)==0:
        return 1
    else:
        print "length of satisfy is "+str(len(satisfy))
        return len(satisfy)

#2
def selectrandomclause():
    import random
    print "the set of unsatisfied clause are "+str(unsatisfy)
    randomclause=random.choice(unsatisfy)
    print "the random clause is "+str(randomclause)
    return randomclause

def randomprobability():
    import random
    p=random.uniform(0,0.5)
    if p>0.5:
       print "the probability is greater"+str(p)
    else:
        print "the probability is less "+str(p)
    return p

def randomliteralselect(clause):
    import random
    literal=random.choice(clause)
    print "the literal selected is "+str(literal)
    return literal

def flipvalue(modelt,literal):

    print "came inside flipvalue "
    lenliteral=len(literal)
    if '~' not in literal: #== 3:
        print "our literal is of length 3"
        player = literal[1]
        player=int(player)-1
        table = literal[2]
        table=int(table)-1
        print "player and table are "+str(player)+" "+str(table)
        value = modelt[player][table]
        print "value in flipliteral is "+str(value)
        print "value is " + str(value)
        if value == 1:
            print "now flip it to 0"
            modelt[player][table] = 0
        elif value == 0:
            print "now flip it to 1"
            modelt[player][table] = 1
        value=modelt[player][value]
        print "value in flipliteral is " + str(value)
    else:
        print "our literal is of length 4"
        if '~' in literal:# lenliteral == 4:
            player = literal[2]
            player=int(player)-1
            table = literal[3]
            table=int(table)-1
            value = modelt[player][table]
            print "value is "+str(value)
            if value == 1:
                print "now flip it 0 len 4"
                modelt[player][table]=0
            elif value==0:
                print "now flip it 1 len 4"
                modelt[player][table]=1

    print "value inside flipvalue is "+str(findvalue(modelt, literal))
    return modelt
#dont iterate the loop
def getmaxflipliteral(model,literal):

    #This function will maintain a dictionary of values between each clause and its maxflip value.
    #we need to slect that clause which has highes len(satisfy) value and return it.
    value=findvalue(model,literal)
    print "value here in test "+str(value)
    length=len(literal)
    if '~'not in literal:
        parent=literal[1]
        parent=int(parent)-1
        table=literal[2]
        table=int(table)-1
    if '~' in literal:
        parent=literal[2]
        parent=int(parent)-1
        table=literal[3]
        table=int(table)-1
    if value==1:
        model[parent][table]=0
        value1=findvalue(model,literal)
        print "value 1 here in test " + str(value1)
    elif value==0:

        model[parent][table]=1
        value1 = findvalue(model, literal)
        print "value 2 here in test " + str(value1)
    print "here the same value is " + str(findvalue(model,literal))
    res1=modelsatisfy(model)
    print "result in maxflip is "+str(res1)
    if res1==1:
        print "result 1 is "+str(res1)
        return -1
    else:
        print "result 1 is " + str(res1)
        return res1

def findvalue(modeltest,literal):

    if   '~' not in literal: #len(literal)==3:
        player=literal[1]
        player=int(player)-1
        table=literal[2]
        table=int(table)-1
    else:
        if '~' in literal: #len(literal)==4:
            player = literal[2]
            player = int(player)-1
            table = literal[3]
            table = int(table)-1
    print "player is "+str(player)
    print "table is "+str(table)
    return modeltest[player][table]
def printmodel(model):
    fh = open('output.txt', 'w')
    fh.write("yes"+"\n")
    #print "model here is "+str(model)
    numrows=len(model)
    numcols=len(model[0])
    #print "numrows is "+str(numrows)
    #print "numcols is "+str(numcols)
    for i in range(0,numrows):
        for j in range(0,numcols):
            #print "i and j are "+str(i)+" "+str(j)
            if model[i][j]==1:
                fh.write(str(i+1)+' '+str(j+1)+"\n")
    fh.close()




if __name__ == '__main__':
    main()
    createClause1()
    createClause2()
    createClause3()
    print "totalclause is "+str(totalclause)
    print "length of totalclause is "+str(len(totalclause))
    #print "total vlause till here is"+str(totalclause)
    #result=PlResolution()
    model=walksat()
    print "model here is "+str(model)
    printmodel(model)
    #print "model is "+str(model)