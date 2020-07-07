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
Matrix = np.array([[3.0, -1.0, 4.0],[17.0, 2.0, 1.0],[1.0, 12.0, -77.0]])
'''
print('Type 1 by 1 the terms of the column vector: ')
Column_Matrix = []
for t in range(Rows):
	vector_aux = []
	vector_aux.append(float(input()))
	Column_Matrix.append(vector_aux)
Column_Matrix = np.array(Column_Matrix)
'''
Column_Matrix = np.array([[2.0],[14.0],[54.0]])

os.system('clear')
print(Matrix); print('\n'); print(Column_Matrix);
Steps_option = input('\nTo shows steps type \'Yes\' otherwise  click \'enter\':\n')
input('\nClick enter to calculate')
os.system('clear')

Expanded_Matrix = []
for t in range (Rows):
	vector_aux = []
	vector_aux = np.append(Matrix[t], Column_Matrix[t])
	Expanded_Matrix.append(vector_aux)
Expanded_Matrix = np.array(Expanded_Matrix)
print('Expanded Matrix')
print('-------------------------------\n');print(Expanded_Matrix); print('-------------------------------\n')

for t in range(Rows):
	if Expanded_Matrix[t][t] != 1:
		Aux = Expanded_Matrix[t][t]
		for o in range(Columns+1):
			Expanded_Matrix[t][o] /= Aux
		if Steps_option == 'Yes': print(Expanded_Matrix); print('\n')

	for n in range(Rows):
		if n != t:
			Aux2 = Expanded_Matrix[n][t]
			for o in range(Columns+1):
				Expanded_Matrix[n][o] = -Aux2*Expanded_Matrix[t][o]+Expanded_Matrix[n][o]#Aux2
			if Steps_option == 'Yes': print(Expanded_Matrix); print('\n')
			
print('Gauss Jordan Matrix')
print('-------------------------------\n');print(Expanded_Matrix); print('-------------------------------\n')