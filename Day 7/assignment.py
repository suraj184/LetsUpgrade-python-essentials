# Assignemnt : 1 

port1 = {21: "FTP", 22:"SSH", 23: "telnet", 80: "http"}
dict2 ={value:key         for key,value in port1.items()}
print("The output:",dict2)

# Assignemnt : 2

list1=[(1,2), (3,4), (5,6),(4,5)]
list2=[]
for each in range(len(list1)):
    b=len(list1[each])
    a=list1[each][b-2]+list1[each][b-1]
    list2.append(a)
print("2) Input is -->",list1,"\n   output is ->",list2)

# Assignemnt : 3

list3=[(1,2,3), [1,2], ['a','hit','less']]
list4=[]
list4=[i for each in list1 for i in each]
print ("The required output-->",list4)
