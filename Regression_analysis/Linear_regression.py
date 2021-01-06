import os
import numpy as np
import matplotlib.pyplot as plt
import tkinter
from tkinter import filedialog
from statistics import mean

os.system('clear')	#clean terminal (cmd windows)

def open_file():
	global f
	f = open('datos3.txt', 'r') #For write the path directly
	######This block is for opne file browser
	'''
	main_win = tkinter.Tk() 
	main_win.withdraw()
	input('Click enter to open explorer file... ')
	current_dir = os.getcwd()
	name_file = filedialog.askopenfilename(initialdir = current_dir)
	main_win.destroy()
	f = open(name_file, 'r')'''
	######

def file_data_to_list_matrix():
	global f
	matrix_ = [];
	matrix_ = [line.split() for line in f]
	return matrix_

def close_file():
	global f
	f.close()

def list_matrix_to_float_vectors(matrix_):
	X_ = []; Y_ = [];
	for n in range(len(matrix_)):
		X_.append(float(matrix_[n][0]))
		Y_.append(float(matrix_[n][1]))
	return X_, Y_

def summations(X_, Y_):
	#Sums that method requires
	Sum_x_  = sum(X_)
	Sum_y_  = sum(Y_)
	Sum2_x_ = (sum(X_))**2
	Prom_y_ = mean(Y_)
	Sum_x2_ = 0; Sum_xy_ = 0;
	n = len(X_)
	for n in range(len(X_)):
		Sum_x2_ += X_[n]**2
		Sum_xy_ += X_[n]*Y_[n]
	return Sum_x_, Sum_y_, Sum2_x_, Prom_y_, Sum_x2_, Sum_xy_, n

def get_alpha_beta_values(Sum_x_, Sum_y_, Sum2_x_, Prom_y_, Sum_x2_, Sum_xy_, n_):
	aux_denominator = n_*Sum_x2_ - Sum2_x_
	alpha_ = (Sum_x2_*Sum_y_ - Sum_x_*Sum_xy_) /aux_denominator;
	beta_  = (n_*Sum_x2_ - Sum_x_*Sum_y_) /aux_denominator;
	return alpha_, beta_

def linear_regression(alpha_, beta_, X_, n_):
	Y_reg_ = []
	for n in range(n_+1):
		Y_reg_.append(alpha_ + beta_*X_[n])
	print('Linear regression: ' + str(alpha_) + ' + ' + str(beta_) + 'X')
	return Y_reg_


def plotting_regression(X_, Y_, Y_reg_, alpha_, beta_):
	plt.title('Linear regression')
	plt.xlabel('x')
	plt.ylabel('y')
	plt.plot(X_,Y_, '.', label="Data")
	plt.plot(X_,Y_reg_, '-', label="Regression")
	plt.legend()
	plt.annotate(str("{0:.6f}".format(alpha_)) + ' + ' + str("{0:.6f}".format(beta_)) + 'X', xy=(1, 80*max(Y_)/100))
	plt.show()


open_file()
matrix = file_data_to_list_matrix()
close_file()
X, Y = list_matrix_to_float_vectors(matrix)
Sum_x, Sum_y, Sum2_x, Prom_y, Sum_x2, Sum_xy, n = summations(X, Y)
alpha, beta = get_alpha_beta_values(Sum_x, Sum_y, Sum2_x, Prom_y, Sum_x2, Sum_xy, n)
Y_reg = linear_regression(alpha, beta, X, n)
plotting_regression(X, Y, Y_reg, alpha, beta,)