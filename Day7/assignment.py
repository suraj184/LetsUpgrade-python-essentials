# Assignemnt : 1 

port1 = {21: "FTP", 22:"SSH", 23: "telnet", 80: "http"}
k=list(port1.keys())
v=list(port1.values())
dict1={}
for each in range(len(k)):
    dict1[v[each]]=k[each]
print("Input is ",port1,"\noutput is ",dict1)

# Assignemnt : 2

list1=[(1,2), (3,4), (5,6),(4,5)]
list2=[]
for each in range(len(list1)):
    b=len(list1[each])
    a=list1[each][b-2]+list1[each][b-1]
    list2.append(a)
print("Input is ",list1,"\noutput is ",list2)

# Assignemnt : 3

import random as rd
list3=[(1,2,3), [1,2], ['a','hit','less']]
list4=[]
x,y,z=list3
d,e,f=x
list4=y+z
for each in range(len(x)):
    list4.append(x[each])  
print(list4)
