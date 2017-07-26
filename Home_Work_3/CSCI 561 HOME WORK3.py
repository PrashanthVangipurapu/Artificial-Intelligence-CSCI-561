class Query:
    children = {}
    parents={}
    def __init__(self,lineq):
        print 'lineq is '+str(lineq)
        self.process(lineq)
        #print "constructor invoked"
    def process(self,lineq):
        print "query processing method is invoked wit query "+str(lineq)
        if lineq[0]=='P':
            self.type='P'
        elif lineq[0]=='E':
            self.type='E'
        elif lineq[0]=='M':
            self.type='M'
        else:
            return None
        start=0
        end=0
        for i in range(len(lineq)):
            if lineq[i]=='(':
                start=i
            elif lineq[i]==')':
                end=i
        actquery=lineq[start+1:end]
        print "Actual query is "+str(actquery)

        if '|' in actquery :
            print "there is a condition"
            spliq=actquery.split('|')
            print 'spliq is '+str(spliq)
            if ',' in spliq[0]:
                print 'more than one children'
                children=spliq[0].split(',')
                print 'more than one children after split is '+str(children)
                for i in range(len(children)):
                    children[i]=children[i].strip()
                print 'more than 1 childrern after strip split '+str(children)

            else:
                 children=spliq[0]


            parents=spliq[1]
            print "parents after codnition split "+str(parents)
            self.finetune(self.type,children,parents)
        else:
            #print "There is no condition."
            print "actquery is "+str(actquery)
            if ',' in actquery:
              print 'joint probability'
              spliq=actquery.split(',')
              print 'spliq is after , '+str(spliq)
            else:
                spliq="".join(actquery.split())
                spliq=spliq.split()
            #    print 'expected utility or meu'
            #    print "spliq is "+str(spliq)
            children=spliq
            parents=[]
            print 'children are '+str(children)
            self.children = {}
            self.parents = {}
            # *********This loop is used only for children************.
            for i in range(len(spliq)):
                print 'children number '+str(i)
                self.finetune(self.type,spliq[i], parents)
            #print "children and parents are "+str(children)+' '+str(parents)
    def finetune(self,type1,child,par):

        #maintain one dictionary for p type children and e type children and list for m type children as their children doesn't have any + or -
        print 'child in finetune  '+str(child)
        print 'parent in fintune '+str(par)+' type of parent is '+str(type(par))
        if type(par)!= list:
            #print 'condition loop called'
            #print "parents in no condition loop  "+str(par)
            parent=par.split(',')
            print 'parent in query is  '+str(parent)
            #print "parent break is "+str(parent)
            for each in parent:
             #   print "parent of each is "+str(each)
                subparent = each.split('=')
                print 'subparent at split = is '+str(subparent)

                print 'subparent in query is '+str(subparent)
                for i in range(len(subparent)):
                    subparent[i]=subparent[i].strip()
                print 'new subparent is ' + str(subparent)
                l2 = "".join(subparent[1].split())
                print 'new subparent is '+str(l2)
                if l2 == '+':
              #      print "has positive value"
                    self.parents[subparent[0]] = 1
                else:
               #     print "has negative value"
                    self.parents[subparent[0]] = 0
        #print "parents dictionary is "+str(self.parents)
        print "children before split is "+str(child)

        childc=child
        print 'childc is '+str(childc)
        children=childc.split('=')
        print 'children after split is '+str(children)
        for i in range(len(children)):
             children[i] = children[i].strip()
        print 'children after split strip is ' + str(children)
        #print "children are " + str(children)
        if type1 == 'P' or type1 == 'E':
           #print "came inside this type"
            l2 = "".join(children[1].split())
           #print "Length of child string is "+str(len(child))
            if l2=='+':
              #print 'self.child '+str(self.children[0])
              self.children[children[0]]=1
            else:
              self.children[children[0]]=0

        else:
            #print "in type meu"
            #print len(child)
            child1=child.split()
            self.children=child1
            #print "meu children "+str(self.children)
        #Conditions dictionary. Since each condition will have + and - so no need to check them.
        #self.parents={}


        print 'children and parent after modification is '+str(self.children)+' '+str(self.parents)

    def __str__(self):
        #print "Task str invoked"
        #print self.type
        #print self.query
        #print self.condition
        #print "came back"
        stri='type=%s' % self.type
        stri+=' children=%s' %self.children
        stri+=' parents=%s' %self.parents
        #string = 'Type = %s, children = %s, parents = %s' % (self.type, self.children, self.parents)
        print "task string is "+stri
        return stri

    __repr__ = __str__


class probTable:

   def __init__(self):
       self.decision=False
       self.alldict={}

   def processdata(self,datalist):
       query=[]
       print 'the sentences given are '+str(datalist)

       utilcheck=datalist[0]
       print 'utilcheck is '+str(utilcheck)
       utsp=utilcheck.strip().split('|')
       # print "split utilcheck is "+str(utsp)
       if utsp[0].strip(' ')=='utility':
           # print 'there is a utility node'
           # print 'its parents are '+str(utsp[1])
           self.decision, self.name, self.childname, self.parents, self.table = self.processnode(datalist)
           list=[self.decision,self.name,self.parents,self.table]
           self.formdict(self.childname,list)
           # print 'done here now'
           return self.alldict
       else:
         # print 'not a utility node '
         # print 'length of datalist is '+str(len(datalist))
         for i in range(0,len(datalist)):
           # print 'processed datalist[i] is '+str(datalist[i])
           if datalist[i].strip('\n\r\t') == '***':
               # print '3 star found'
               self.decision, self.name, self.childname, self.parents, self.table = self.processnode(query)
               query = []
               list = [self.decision,self.name, self.parents, self.table]
               self.formdict(self.childname,list)
               #return self.alldict
           else:
               query.append(datalist[i])
         # print 'query outside is '+str(query)
         self.decision, self.name, self.children, self.parents, self.table=self.processnode(query)
         list = [self.decision,self.name, self.parents, self.table]
         self.formdict(self.children, list)
         # print 'at end alldict is '+str(self.alldict)
         return self.alldict

   def formdict(self,name,lis):
       # print 'alldict till now is '+str(self.alldict)
       self.alldict[name]=lis

   def processnode(self,query):
       print 'the given node at processnode is '+str(query)
       name=query[0]
       print 'name at q[0] is '+str(name)
       if '|' in name:
           # print 'it has parents'
           childsp=name.split('|')
           print 'childsp is '+str(childsp)
           for i in range(len(childsp)):
               childsp[i]=childsp[i].strip()
           print 'childsp now is '+str(childsp)

           childname=childsp[0]
           print 'len of childname is '+str(len(childname))
       else:
           # print 'it has no parents'
           childname=name
       # print 'given name is '+str(name)
       # print 'childname is '+str(childname)
       if len(query)!=0:
           charat=query[0]
           # print "charat is "+str(charat)
           child=childname
           # print 'child is '+str(child)


           # This loop is used only for getting parents only for the given child node.
           if '|' in charat:
               # Our child node has parents
               par=charat.split('|')
               # print 'par is '+str(par)
               if len(par[1].strip())>1:  #This checks length of string.
                   # print 'there are more than one parent'
                   print 'par[1] is '+str(par[1])
                   parents=par[1].split()
                   print 'parents after splting at , '+str(parents)
                   # numpar=len(parents)

               else:
                   # print 'there are less than two parent'
                   # numpar=1
                   # print "par[1] is "+str(par[1])
                   p=par[1].strip()
                   parents=list()
                   parents.append(p)
                   print 'parents now is '+str(parents)
           else:
               #our child node doesn't have any parents.
               # print 'no parents'
               parents=[]
           # print 'parents are '+str(parents)
           # This loop is used only for getting parents only for the given child node.
           #checked for nodes till now

           table=[]
            #we came to knwow about the parents. Now fill the probability table.
           if query[1].strip() != 'decision':
               # print 'not a decision node'
               if len(parents)>0:
                  # print 'parents inside if are '+str(parents)
                  #parentact=parents[0].replace(" ","")
                  # print 'parentact is '+str(parentact)
                  lenp=len(parents)
                  # print 'lenp is '+str(lenp)
                  table=[0]*(2**lenp)
                  for each in query[1:]:
                      value=each.split()
                      # print 'value before updating table '+str(value)
                      #table[]
                      # print 'table for updation '+str(table)
                      table=self.filltable(value,table)
               else:
                   # print 'no parents are there'
                   table.append(query[1])
               print 'table et end is '+str(table)
               self.decision = False
               print 'decsion at end is '+str(self.decision)

               return self.decision, name, childname, parents, table

           else:
               self.decision= True
               return self.decision, name, childname, parents, table

   def filltable(self,value,table):
       # print 'value is '+str(value)
       # print 'table is '+str(table)
       # print 'lenp is '+str(lenp)
       mydict={'+':1,'-':0}
       rsum=0
       # print 'lenp is '+str(lenp)
       bolval=[]
       for i in range(1,len(value)):
           par1=value[i]
           bolval.append(mydict[par1])

       # print 'bolval is '+str(bolval)
       l = len(bolval) - 1
       rsum = 0
       for i, e in reversed(list(enumerate(bolval))):
           b = l - i
           p = 2 ** b
           rsum = rsum + p * e
       table[rsum]=value[0]
       # print 'table in this function '+str(table)
       return table

   def __str__(self):
       string = 'Name = %s, Parents = %s, Prob_table = %s, Decision = %s' % (
           self.name, self.parents, self.table, self.decision)
       return string

   __repr__ = __str__
def process_infile():
    queries=[] #This will contain each and every query as an list of objects
    f=open('input1.txt','r')
    #print "Filename passed is "+str(f)
    sixflag=0
    #with open(f) as f1:
    line=f.readline()
    gettable=[]
    getutility=[]
    while len(line)!=0:
            line = line.strip('\t\n\r')
            # print "line is "+str(line)
            if line=='******':
              # print "completed reading all tasks"
              sixflag = sixflag + 1
              line = f.readline()
              continue
            if sixflag==0:
                print "task to be read is "+str(line)
                q=Query(line)
                print "value of object q is "+str(q)
                queries.append(q)
            elif sixflag==1:
                #print 'completed reading queries. start reading table now'
                gettable.append(line)
            elif sixflag == 2:
                # print 'completed reading tABLE Also. start reading utility'
                getutility.append(line)
            line = f.readline()
    print 'queries at end are '+str(queries)
    #print 'table sentences are '+str(gettable)
    #print 'utility sentences are '+str(getutility)
    t=probTable()
    #print 't is '+str(t)
    table=t.processdata(gettable) #calling a class.
    print 'table we got at end is '+str(table)
    # print 'type of table is '+str(type(table))


    #process utility nodes now
    # print 'utility sentences are '+str(getutility)
    print 'creating second object '
    t1=probTable()
    #print 't1 is '+str(t1)
    print 'getutility is '+str(getutility)
    if len(getutility)!=0:
       utility=t1.processdata(getutility)
    else:
        utility= None
    # print 'utility node is '+str(utility)
    # print 'check for this '+ str(t1 is t)
    #print "The whole queries are "
    return queries, table, utility


def pQuery(child,parent,table):
    print 'Inside pQuery'
    #print 'child at p type is '+str(child)
    #print 'parent at p type is '+str(parent)
    #print 'table at ptype is '+str(table)
    print 'type of child is '+str((child))
    print 'type of parent is '+str((parent))
    for each in child.keys():
        if each in parent.keys():
            if child[each] != parent [each]:
                return 0.00

    print 'its parent is ' + str(parent)
    c=child.copy()
    print 'c before update is ' + str(c)
    c.update(parent)

    #c.update(parent)
    print 'c  is '+str(c)
    print 'first time'
    res1=findval(c,table)
    print 'value of prob 0 is '+str(res1)
    res2=findval(parent,table)
    print 'value of prob 1 is ' + str(res2)
    final=res1/res2
    return final

def findval(query,table):
    # table order is decision, name, parents, table.
    #print 'In findval'
    if len(query)==0:
        return float(1)
    print 'in findval queries '+str(query)
    print 'in findval table is '+str(table)
    boolt=True
    for k in query:
        print 'query is '+str(query)
        print 'key is '+str(k)

        if k in table.keys(): #extra
            parent=table[k][2]
            print 'table of '+str(k)+' is '+str(parent)
            print 'iterkey check key is '+str(parent)
            for each in parent:
                print 'parent node is '+str(each)
                print 'type of parent node is ' + str(type(each))
                if each not in query.keys():
                    print each +' not there in query keys'
                    print 'boolt is false'
                    boolt=False
                    break
            if boolt == False:
                print 'boolt is false '
                break

    if boolt == True:
        print ' boolt is true '
        res=1
        for each in query.keys():
            print 'each is '+str(each)
            print 'table ypu are check is '+str(table)
            if each in table.keys():
                if table[each][0] :
                    print 'continue'
                    continue
                i = 0
                parent=table[each][2]
                for p in parent:
                    print "parent name is  "+str(p)
                    if p in query.keys():
                        print 'what is this ?  '+str(query[p])
                        i = (i << 1) + query[p]
                        print 'index is '+str(i)
                print 'came for first time'
                if query[each]:
                   res = res * float(table[each][3][i])
                   print 'result for first time at one' + str(res)
                else:
                    print 'came here for first time in else 2'
                    print 'its value is '+str(float(table[each][3][i]))
                    print '1- value is '+str(1 - float(table[each][3][i]))
                    print 'value of res is '+str(res)
                    res =res *(1 - float(table[each][3][i]))
                    print 'result for first time at two' + str(res)
        print 'result in answer_p is '+str(res)
        return res

    for each in query.keys():
        print 'in for loop '
        i = 0
        if each in table.keys():
            parent = table[each][2]
            for p in parent:
                if p not in query.keys():
                    p1=p
                    new1=dict(query)
                    new1[p1]=0
                    new2=dict(query)
                    new2[p1]=1
                    res= findval (new1,table) + findval(new2,table)

    return res

def adddict(parents,count):
    c=count
    res={}
    newp=parents[::-1]
    for i in range (len(newp)):
        res[parents[i]]= c % 2
        c=c / 2

    return res


def eQuery(children,parents,ptable,utility):

    res=0
    print 'parents of utility are '+str(utility)
    #print 'type of utility is '+str(type(utility))
    #print 'keys of utility are '+str(utility.keys())
    print 'utility is '+str(utility)
    print 'parents of utility are '+str(utility['utility'][2])
    up=utility['utility'][2]
    lenp=len(up)
    lenp1= 2**lenp
    for i in range(lenp1):
        q=adddict(up,i)
        p=children
        p.update(parents)
        if True:
           print 'new_query is ' + str(q)
           print 'new condtion is '+str(p)
           #print 'table is '+str(ptable)
           #print 'this value is '+str(utility['utility'][3][i])+' and its type is '+str(type(utility['utility'][3][i]))
           #print 'utility prob value is '+str(utility['utility'][3][i])
           #print 'askp utility value is '+str(type(pQuery(q,p,ptable)))
           r1= utility['utility'][3][i]
           r2= pQuery(q,p,ptable)
           r3=float(r1)*float(r2)
           #r4=float(r1)
           res=res+r3
           #print 'res in this loop is '+str(res)
           #print 'r3,r4' + str(r3)+' '+str(r4)
           #res=res + (utility['utility'][3][i] * pQuery(q,p,ptable))
           print 'result in this loop is '+str(res)
    print 'result of eu is '+str(res)
    return res
def addlist(maxi,len1):
    i1 = maxi
    res=[]
    if maxi >> (2 ** len1 -1):
        return None
    for i in range(len1-1,-1,-1):
        ind=i >> 2
        if ind==0:
            res.append('-')
        else:
            res.append('+')
            i1=i1-ind * 2** i
    print ' result is in list'+str(res)
    return res



def mQuery(children,parents,ptable,utility):

    print 'children are '+str(children)
    print 'parents are '+str(parents)
    max= -9999999.0
    maxi=0
    lenp = 2**len(children)
    for i in range(lenp):
        q=adddict(children, i)
        resu= eQuery(q,parents,ptable,utility)
        if resu > max :
            max=resu
            maxi=i
    res1= addlist(maxi,len(children))
    value1=res1[0]
    return value1,max
def myround(value):
    if value<0:
        val1= -(value)
        a=int(round(val1))
        return a
    if value>0 :
        val1=value
        a=int (round(val1))
        return a

def writeoutput(queries,table,utility):
    #table order is decision, name, parents, table.
    print 'queries are '+str(queries)
    with open('output1.txt','w') as f:
        for i in range(len(queries)):
            #print 'each task is '+str(queries[i])
            print queries[i].type
            #print 'table is '+str(table)
            if queries[i].type == 'P':
                print 'calling pquery'
                print 'queries[i],chikd '+str(queries[i].children)
                res=pQuery (queries[i].children, queries[i].parents,table)
                print 'returned result is '+str(res)
                a=str(round(res,2))
                f.write(a)
                f.write('\n')
            if queries[i].type == 'E':
                res=eQuery(queries[i].children, queries[i].parents,table,utility)
                print 'res of ask eu is '+str(res)
                a=myround(res)
                s=str(a)
                f.write(s)
                f.write('\n')
            if queries[i].type == 'M':
                res= mQuery(queries[i].children, queries[i].parents, table, utility)
                print 'res of ask meu is '+str(res)
                val1=res[0]
                val2=res[1]
                print 'val1 and val2 are '+str(val1)+' '+str(val2)
                retval=myround(val2)
                retval=val1+' '+str(retval)
                f.write(retval)
                f.write('\n')
def main():
    queries, table, utility= process_infile()
    print 'returned query is '+str(queries)
    print 'returned table is '+str(table)
    print 'returned utility is '+str(utility)
    writeoutput(queries,table,utility)

if __name__=='__main__':
   main()