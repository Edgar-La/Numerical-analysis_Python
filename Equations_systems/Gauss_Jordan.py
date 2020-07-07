''' Gauus Jordan method to solve equations of n-variables
	jun 07, 2020
	By Edgar
'''
import os
os.system('clear')
import numpy as np
print('WELCOME TO EQUATIONS SYSTEMS SOLVER\n')
Rows = int(input('Type tu number of unknows variables: '))
Columns = Rows

print('\nType 1 by 1 the terms of the equations matrix: ')
Matrix = []
for t in range(Rows):
	vector_aux = []
	for o in range(Columns):
		vector_aux.append(float(input()))
	Matrix.append(vector_aux)
Matrix = np.array(Matrix)

print('\nType 1 by 1 the terms of the column vector: ')
Column_Matrix = []
for t in range(Rows):
	vector_aux = []
	vector_aux.append(float(input()))
	Column_Matrix.append(vector_aux)
Column_Matrix = np.array(Column_Matrix)

os.system('clear')
print(Matrix); print('\n'); print(Column_Matrix);
Steps_option = input('\nTo shows steps type \'yes\' otherwise  click \'enter\':\n')
input('\nOk. Click enter to calculate')
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
		if Steps_option == 'yes': print(Expanded_Matrix); print('\n')

	for n in range(Rows):
		if n != t:
			Aux2 = Expanded_Matrix[n][t]
			for o in range(Columns+1):
				Expanded_Matrix[n][o] = -Aux2*Expanded_Matrix[t][o]+Expanded_Matrix[n][o]#Aux2
			if Steps_option == 'yes': print(Expanded_Matrix); print('\n')

print('Gauss Jordan Matrix')
print('-------------------------------\n');print(Expanded_Matrix); print('-------------------------------\n')