import os
os.system('clear')
import numpy as np

#Rows = int(input('Type tu number of rows: '))
#Columns = int(input('Type tu number of columns: '))
Rows = 3
Columns = 3
os.system('clear')
'''
print('Type 1 by 1 the terms of the equations matrix: ')
Matrix = []
for t in range(Rows):
	vector_aux = []
	for o in range(Columns):
		vector_aux.append(float(input()))
	Matrix.append(vector_aux)
Matrix = np.array(Matrix)
'''
Matrix = np.array([[3, -1, 4],[17, 2, 1],[1, 12, -77]])
'''
print('Type 1 by 1 the terms of the column vector: ')
Column_Matrix = []
for t in range(Rows):
	vector_aux = []
	vector_aux.append(float(input()))
	Column_Matrix.append(vector_aux)
Column_Matrix = np.array(Column_Matrix)
'''
Column_Matrix = np.array([[2],[14],[54]])

os.system('clear')
print(Matrix); print('\n'); print(Column_Matrix); input('\nClick enter to calculate')

Expanded_Matrix = []
for t in range (Rows):
	vector_aux = []
	vector_aux = np.append(Matrix[t], Column_Matrix[t])
	Expanded_Matrix.append(vector_aux)
Expanded_Matrix = np.array(Expanded_Matrix)
	#print(Expanded_Matrix[t])

print('\n');print(Expanded_Matrix)

#print(Expanded_Matrix)