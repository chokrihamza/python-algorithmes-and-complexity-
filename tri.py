import random
"""## bubble sort

A=[1,22,5,10,12,14,20,20,5,44,60,12]
# i=0 1,22,5,10,12,14,20,5,44,12,         60
# i=1 1,22,5,10,12,14,20,5,12,         44
def tri_bubble(table):
    if len(table)==0:
        return "please enter a valid table"
    for i in range(len(table)-1):
        for j in range(len(table)-i-1):
            if table[j]>table[j+1]:
                change=table[j]
                table[j]=table[j+1]
                table[j + 1]=change
    return table

#print(tri_bubble(A))


## bubble sort



a=[43,5,8,4,6,7,3]
def triabulle(tableau):
    for i in range(len(tableau)-1):
        for j in range(len(tableau)-1-i):
            if tableau[j]>tableau[j+1]:
                change=tableau[j]
                tableau[j]=tableau[j+1]
                tableau[j + 1]=change
    return(tableau)
#print(triabulle(a))

B=[1,22,5,10,12,14,20,20,5,44,60,12]
def recherche(table,but):
    for i in range(len(table)):
        if table[i]==but:
           return "T["+str(i)+"]:"+str(table[i])
    return False
#print(recherche(B,60))

# binary search # recherche dichotomie
# tableau trié
# target 50
#  0 1 2 3 4 5 6 7 8 9  10 11 12 13 14 15 16
C=[1,2,3,4,5,6,7,8,9,10,40,50,52,53,60,80,100]

def binary_search(table,target):
    low=0
    high=len(table)-1
    while low<=high:
        mid=(low+high)//2
        if table[mid]==target:
            return table[mid]
        if table[mid]<target:
            low=mid+1
        elif table[mid]>target:
            high=mid-1
    return False

#print(binary_search(C,20))

aymen=""
n=10
#for i in range(n-1):

 #   k=str(input("enter l'element"+str(i)+ "\n"))
  #  aymen=aymen+k
#print(aymen)


c=5
for i in range(5):
    c=c+3
print(c)

# convch(x,)

# convch(100,benali)
# ch="100"""
def remplirid(n):
    tableau=[]
    if 3<=n<=50:
        for i in range(n):
            k=int(input())
            if len(str(k))==8:
                tableau.append(k)
            else:
                print("please enter a number of 8 digits")

    return tableau

#IDENT=remplirid(10)
#print(IDENT)
def remplirdate(n):
    tableau=[]
    if 3<=n<=50:
        for i in range(n):
            print("enter the day")
            j=int(input())
            print("enter the month")
            m=int(input())
            if 1<=j<=31 and 1<=m<=12:
                k=str(j)+"/"+str(m)
                tableau.append(k)
            else:
                print("please enter a valid date")

    return tableau
#date=remplirdate(4)
#print(date)
def code(date):
    t=[]
    coderandom=[]
    for i in range(len(date)):
        valstr=str(date[i])
        t.append(valstr.replace("/",""))

    for j in range(len(t)):
        k=int(t[j])*random.randint(60,64)
        if len(str(k))>4:
            val=int(str(k)[0:3]+str(k)[3:])

            coderandom.append(val)
    return coderandom
# Algorthme Code_entreprise_X
# variables:
# date
# n<--10
#Debut
# date <--remplirdate(n)
IDENT=remplirid(4)
print(IDENT)
date=remplirdate(4)
print(date)
print(code(date))
#Fin