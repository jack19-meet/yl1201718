a=[5,10,15,20,25]
b=[]
def list1(a):
	b=[a[0],a[-1]]
	return b
print (list1(a))



y=[1,2,3,1,1,4,5,6,78,90,69]
for i in range(len(y)):
	if y[i]<5:
		print(y[i])





a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
for value in a:
	if value in b:
		print(value)


import random
x=random.randint