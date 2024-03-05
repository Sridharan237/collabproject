#program for sum of two matrices

m1 = [[1,2,3],[4,5,6]]
m2 = [[1,2,3],[4,5,6]]

m3 = list()

for i in m1:
	for j in m2:
		m3.append(i+j) 

print("sum is : ", m3)