'''	This program calculates polynomial regression of any .txt file
	This code will be 'larger' because we won´t use any math module.
	jul 08, 2020
	By Edgar Lara
'''

import os
os.system('clear')
import numpy as np
import matplotlib.pyplot as plt
import tkinter
from tkinter import filedialog
main_win = tkinter.Tk() 
main_win.withdraw()

#def file_to_vectors_(name):
def file_to_vectors_():
	input('Click enter to open explorer file	')
	#f = open(name, 'r')
	current_dir = os.getcwd()
	name = filedialog.askopenfilename(initialdir= current_dir)
	main_win.destroy()
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
					matrix_[n][o] = -Aux2*matrix_[t][o]+matrix_[n][o]
	return matrix_

def regression_function(Gauss_jordan_matrix_, X_):
	global function_str; function_str = ''
	print('\n\nThe regression is:')
	for t in range(order, -1, -1):
		function_str += str(Gauss_jordan_matrix_[t][order+1])+'X^'+str(t)+' + '
	print(function_str + '\n')

	Xsmooth_ = np.arange(min(X_), max(X_), 0.5)
	Ysmooth_ = []
	for t in range(0, len(Xsmooth_)):
		aux = 0
		for o in range(order, -1, -1):
			aux += Gauss_jordan_matrix_[o][order+1]*np.power(Xsmooth_[t],o)
		Ysmooth_.append(aux)
	return Xsmooth_, Ysmooth_

def plotting(X_, Y_, Xsmooth_, Ysmooth_):
	input('Click enter to open the graphic	')
	plt.title('Polynomial regression with fit order: ' + str(order))
	plt.plot(X_,Y_, '.', label="Data")
	plt.plot(Xsmooth_, Ysmooth_, label="Regression")
	plt.legend()
	plt.show()

print('WELCOME TO POLyNOMIAL REGRESSION CALCULATOR\n\n')
#file_name = 'datos.txt'
order = int(input('Type order regression:	'))
#X, Y = file_to_vectors_(file_name)
X, Y = file_to_vectors_()
Regression_matrix = regression_matrix_(X, Y)
Gauss_jordan_matrix = Gauss_jordan(Regression_matrix)
Xsmooth, Ysmooth = regression_function(Gauss_jordan_matrix, X)
plotting(X, Y, Xsmooth, Ysmooth)