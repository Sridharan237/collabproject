#program for sum of two matrices

m1 = [[1,2,3],[4,5,6]]
m2 = [[1,2,3],[4,5,6]]

m3 = list()
def change():
for i in m1:
	for j in m2:
		m3.append(i+j) 
	return m3

print(change(m3))
