list1=[10,20,40,60,70,80]
list2=[5,15,25,35,45,55,90]
list3=list1+list2
list4=[]
for each in range(len(list3)):
    a=min(list3)
    list3.remove(a)
    list4.append(a)
print(list4)
