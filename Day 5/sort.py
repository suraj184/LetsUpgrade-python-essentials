list1=[0,10,1,35,0,56,89,0,2,30,0,45,69,0]
list2=[]
for each in list1:
    if each==0:
        list2.append(each)
        list1.remove(each)
list1.sort()
print(list1+list2)
