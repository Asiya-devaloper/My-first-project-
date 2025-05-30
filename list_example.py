#Advance data type.py
#List data structure:
li=[10,20,30,40,50,50,20]
li.append(600)
print(li)#[10,20,30,40,50,50,20,600]
li.Remove(50)#[10,20,30,40,50,20,600]
li.pop()
print(li)#[10,20,30,40,50,20]
#del li[3]and li.pop(3)both are equivalent.
li.pop (3)#[10,20,30,50,20]
del li
#print(li)#Error
L1=[10,20,30,40]
L2=[50,60,70]
L1=L1+L2# [10,20,30,40,50,60,70]