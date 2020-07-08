'''	This program calculates polinomial regression of any .txt file
	This code will be 'larger' because we won´t use any math module.
	jun 08, 2020
	By Edgar Lara
'''

import os
os.system('clear')
import numpy as np
import matplotlib.pyplot as plt

file_name = 'datos2.txt'

def file_to_vectors_(name):
	f = open(name, 'r')
	matrix_ = [];	X_ =[];	Y_ = []
	matrix_ = [line.split() for line in f]
	f.close()
	for t in range(0,len(matrix_)):
		X_.append(float(matrix_[t][0]))
		Y_.append(float(matrix_[t][1]))
	return X_,Y_

def regression_matrix_(X_, Y_):
	matrix_ = []
	extended_vector = []
	for t in range (0, order+1):
		vector_aux = [];	matrix_.append(vector_aux)
	for t in range(0, order+1):
		for o in range(0, order+1):
			matrix_[o].append(	sum(	np.power(X_,(t+o))	)	)
		aux2 = []; aux2.append(	sum(	np.power(X_,t)*Y_	)	)
		extended_vector.append(aux2)
	for t in range(0, order+1):
		matrix_[t].append(extended_vector[t][0])
	return	matrix_

def Gauss_jordan(matrix_):
	for t in range(order+1):
		if matrix_[t][t] != 1:
			Aux = matrix_[t][t]
			for o in range(order+2):
				matrix_[t][o] /= Aux

		for n in range(order+1):
			if n != t:
				Aux2 = matrix_[n][t]
				for o in range(order+2):
					matrix_[n][o] = -Aux2*matrix_[t][o]+matrix_[n][o]#Aux2
	return matrix_
	#print(np.array(matrix_))

def regression_function(Gauss_jordan_matrix_, X_):
	function_str = ''
	print('The regression is:\n')
	for t in range(order, -1, -1):
		function_str += str(Gauss_jordan_matrix_[t][order+1])+'X^'+str(t)+' + '
	print(function_str)

	Xsmooth_ = np.arange(min(X_), max(X_), 0.5)
	#print(Xsmooth_)
	Ysmooth_ = []
	for t in range(0, len(Xsmooth_)):
		aux = 0
		for o in range(order, -1, -1):
			#aux += Gauss_jordan_matrix_[o][3]*(Xsmooth_[t])^o
			aux += Gauss_jordan_matrix_[o][order+1]*np.power(Xsmooth_[t],o)
		Ysmooth_.append(aux)
	return Xsmooth_, Ysmooth_

def plotting(X_, Y_, Xsmooth_, Ysmooth_):
	plt.title('Polinomial regression with fit order: ' + str(order))
	plt.plot(X_,Y_, '.', label="Data")
	plt.plot(Xsmooth_, Ysmooth_, label="Regression")
	plt.legend()
	plt.show()

#global order
order = int(input('Type order regression:	'))
X, Y = file_to_vectors_(file_name)
Regression_matrix = regression_matrix_(X, Y)
Gauss_jordan_matrix = Gauss_jordan(Regression_matrix)
Xsmooth, Ysmooth = regression_function(Gauss_jordan_matrix, X)
plotting(X, Y, Xsmooth, Ysmooth)

#print(np.array(Regression_matrix))
#print(np.array(Gauss_jordan_matrix))