import os
import numpy as np
os.system('clear')
############################################################################
Rows = int(input('Typer the number of rows: '))
Columns = int(input('Typer the number of Columns: '))
os.system('clear')
print('Type 1 by 1 the terms of matrix equations')
M = []
for t in range(Rows):
	h_vector = []
	for o in range(Columns):
		h_vector.append(float(input()))
	M.append(h_vector)
M = np.array(M)
print(M);	print('\n')
############################################################################
print('Type 1 by 1 the terms of column vector results')
r = []
for t in range(Rows):
	data = []
	data.append(float(input()))
	r.append(data)
print(r);	print('\n')
input('Click enter to calculate')
############################################################################
#using assignment operator is not a way to duplicate an array
M1 = M.copy();	M1[0][0] = r[0][0];  M1[1][0] = r[1][0]; M1[2][0] = r[2][0];
M2 = M.copy();	M2[0][1] = r[0][0];  M2[1][1] = r[1][0]; M2[2][1] = r[2][0];
M3 = M.copy();	M3[0][2] = r[0][0];  M3[1][2] = r[1][0]; M3[2][2] = r[2][0];

dM = (M[0][0] *  (M[1][1]* M[2][2]- M[2][1]* M[1][2]) -  M[0][1] *  (M[1][0]* M[2][2]- M[2][0]* M[1][2]) +  M[0][2] * ( M[1][0]* M[2][1]- M[2][0]* M[1][1]))
dM1=(M1[0][0] * (M1[1][1]*M1[2][2]-M1[2][1]*M1[1][2]) - M1[0][1] * (M1[1][0]*M1[2][2]-M1[2][0]*M1[1][2]) + M1[0][2] * (M1[1][0]*M1[2][1]-M1[2][0]*M1[1][1]))
dM2=(M2[0][0] * (M2[1][1]*M2[2][2]-M2[2][1]*M2[1][2]) - M2[0][1] * (M2[1][0]*M2[2][2]-M2[2][0]*M2[1][2]) + M2[0][2] * (M2[1][0]*M2[2][1]-M2[2][0]*M2[1][1]))
dM3=(M3[0][0] * (M3[1][1]*M3[2][2]-M3[2][1]*M3[1][2]) - M3[0][1] * (M3[1][0]*M3[2][2]-M3[2][0]*M3[1][2]) + M3[0][2] * (M3[1][0]*M3[2][1]-M3[2][0]*M3[1][1]))

R = np.array([[dM1/dM], [dM2/dM], [dM3/dM]])
############################################################################
os.system('clear')
print(M); print('\n'); print(r); print('\n')
print("Solutions are: ")
for t in range(Rows): 
    print(R[t][0], end = '\n')
