x=[1,2,1,2,1,2,1,2,1]
for i in x:
	if i==1:
		x.remove(i)
print(x)


x=[1,2,3,4]
y=x
y=x[::]
y=x.copy()
x[0]=999
print(x)
print(y)


x=[3,4,[5,6]]
y=x.copy()
z=x

x[0]=100
x[2][0]=999
print(x)
print(y)
print(z)

import random
alist=list(range(3,18,1))
random.shuffle(alist)
print("before sort")
print(alist)

alist.sort(reverse=True)
alist.sort(key=lambda x:len(str(x)),reverse=True)
print("after sort")
print(alist)


a=[1,2,3]
b=['a','b','c']
ab=zip(a,b)
print(list(ab))

for i,j in ab:
	print(i,j)

a=['a','b','c']
en=enumerate(a)
print(list(en))

for i,item in en:
	print(i,item)

import os
for filename in [filename for filename in os.listdir('.') if filename.endswith(('.py','.pyw'))]:
	print(filename)

# inv
matrix = [ [1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]] 
inv_matrix=[[row[i] for row in matrix] for i in range(4)]
print(inv_matrix)
