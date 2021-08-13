import os
import matplotlib.pyplot as plt
from statistics import mean
from math import log, exp
import tkinter
from tkinter import filedialog

os.system('clear')

def open_file(name_file_):
	global f
	f = open(name_file_, 'r') #Write the dir directly
	

def browse_file():			#Open file browser
	global f
	main_win = tkinter.Tk() 
	main_win.withdraw()
	input('Clic enter to open browser file... ')
	current_dir = os.getcwd()
	name_file_ = filedialog.askopenfilename(initialdir = current_dir)
	main_win.destroy()
	f = open(name_file_, 'r')

def file_to_list_matrix():
	global f; matrix_ = [] 
	matrix_ = [line.split() for line in f]
	return matrix_

def close_file():
	global f
	f.close()

def list_matrix_to_float_vectors(matrix_):
	X_ = []; Y_ = []
	for n in range(len(matrix_)):
		X_.append(float(matrix_[n][0]))
		Y_.append(float(matrix_[n][1]))
		#print(str(X_[n]) + '  ' + str(Y_[n]))
	return X_, Y_

def summations(X_, Y_):
	N = len(X_)
	Sum_x = sum(X_)
	Sum_y = sum(Y)
	Sum_x2 = 0; Sum_xlny = 0; Sum_lny = 0;
	for n in range(N):
		Sum_x2 += X[n]**2
		Sum_xlny += X_[n]*log(Y[n])
		Sum_lny += log(Y[n])
	Sum_2x = Sum_x**2

	return Sum_x, Sum_y, Sum_x2, Sum_xlny, Sum_lny, Sum_2x, N

def get_alpha_beta_values(Sum_x, Sum_y, Sum_x2, Sum_xlny, Sum_lny, Sum_2x, N):
	alpha = (N*(Sum_xlny)-Sum_x*Sum_lny)/(N*Sum_x2-Sum_2x)
	beta = exp((Sum_lny-(alpha*Sum_x))/N)
	return alpha, beta

def exponential_regression(alpha, beta, X_, Y_):
	Y_reg = []
	for n in range(len(X_)):
		Y_reg.append(beta*exp(alpha*X_[n]))
		#print(str(X_[n]) + '  ' + str(Y_[n]) + '  ' + str(Y_reg[n]))
	print('Exponential regression: ' + str(beta) + ' * exp(' + str(alpha) + ' * X)')
	return Y_reg

def correlation_coeficient(X_, Y_, alpha, beta):
	E = 0; S = 0; Y_prom = 0;
	Y_prom = mean(Y_)
	for n in range(len(X_)):
		E += (Y[n] - beta*exp(X[n]*alpha))**2
		S += (Y[n] - Y_prom)**2
	r = ((S -E )/S)**(1/2)
	r2 = r**2
	return r, r2

def plotting(X_, Y_, Y_regr, r_, r2_):
	plt.plot(X_, Y_, '.', label = 'Values')
	plt.plot(X_, Y_reg, '-', label = 'Regression')
	plt.title('Exponential regression')
	plt.xlabel('X')
	plt.ylabel('Y')
	plt.legend()
	plt.annotate(str("{0:.6f}".format(beta)) + 'exp(' + str("{0:.6f}".format(alpha)) + ' * X)', xy = (5, 80*max(Y_reg)/100))
	plt.annotate('r = ' + str("{0:.4f}".format(r)), xy = (5, 70*max(Y_reg)/100))
	plt.annotate('r2 = ' + str("{0:.4f}".format(r2)), xy = (5, 60*max(Y_reg)/100))
	plt.show()


#print('Type file, example: Data.txt')
#fileName = input()
#open_file(fileName)	#Write the dir directly


browse_file()			#Open file browser
matrix = file_to_list_matrix()
close_file()
X, Y = list_matrix_to_float_vectors(matrix)
Sum_x, Sum_y, Sum_x2, Sum_xlny, Sum_lny, Sum_2x, N = summations(X, Y)
alpha, beta = get_alpha_beta_values(Sum_x, Sum_y, Sum_x2, Sum_xlny, Sum_lny, Sum_2x, N)
Y_reg = exponential_regression(alpha, beta, X, Y)
r, r2 = correlation_coeficient(X, Y, alpha, beta)
plotting(X, Y, Y_reg, r, r2)