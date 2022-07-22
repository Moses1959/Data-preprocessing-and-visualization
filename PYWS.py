#question1 :

import string

list=[]
for x in range(2000,3200) :
    if (((x%5)!=0) and ((x%7)==0)) :
        list.append(x)
print(list)

#question2 :

def fact(x):
    if x==0 :
        return 1
    else:
      return x * fact(x-1) 
          
x=int(input("Enter a number : "))
print(fact(x))

#question 3:

n=int(input("Enter a number : "))
dict={}
for i in range(1,n+1):
    dict[i]=i*i
print(dict)

#question 4 :

stri=input("Enter a string :")


while(type(stri)!=str ) :
    stri=input("Enter a valid string")

n=int(input("Enter an index : "))

while((n<0) or (n>=len(stri)) ) :
    n=int(input("Enter a valid index : "))

stri = stri[0 : n : ] + stri[n + 1 : :]
print("The new String : ",stri)

#question 5 :

import numpy as np
na=np.array([[0,1],[2,3],[4,5]])
print("Original array elements : ",na)
na=na.tolist()
print("Array to list : ",na)

#question 6 :

na=np.array([0,1,2])
na2=np.array([2,1,0])

print("Covariance matrix : ",np.cov(na,na2))


#question 7 :

import math
h=30
c=50
values=input("Enter the values of d :")
values=values.split(',')
result=[]
for d in values :
    Q=int(round(math.sqrt(2*c*float(d)/h)))
    result.append(Q)
print(result)


    












