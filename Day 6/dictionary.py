List1=[1,2,3,4,5,6,7]
List2=['a','b','c','d','e']
List3=[]    
[List3.append((List1[each],List2[each])) for each in range(min(len(List1),len(List2)))]
print(dict(List3))
