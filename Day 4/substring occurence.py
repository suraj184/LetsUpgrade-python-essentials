str1 = ("what we think we became; we are python programmer")
print("*Given string is --- 'what we think we became; we are python programmer'")
b=input("Enter letter to check occurence ")
a=-1
c=[]
for each in str1:
    a=a+1
    if str1.index(each)==str1.index(b):
        c.append(a)
print("indices of occurence of ", b, "is ", c)
