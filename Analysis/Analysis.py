# -*- coding: utf-8 -*-
"""
Created on Tue Aug 14 15:22:48 2018

@author: Jarnd
"""
import qiskit.tools.qcvv.tomography as tomo
import Analysis.tomography_functions as tomoself
from qiskit.tools.qi.qi import outer, vectorize, state_fidelity
from qiskit.tools.visualization import plot_state
import numpy as np
from Functions.Create_tomo_circuits import *

def fit_tomodata(tomo_data,method=None):
    if method == 'Linear inversion':
        print('Error, no method yet!')
        choi_fit = []
    elif method == None:
        choi_fit = tomo.fit_tomography_data(tomo_data,options={'trace':4})
    else: 
        choi_fit = tomo.fit_tomography_data(tomo_data,method,options={'trace':4})
    return choi_fit

def fit_chi_own(tomo_data,tomo_set, n):
    B_chi = tomoself.get_pauli_basis(n)
    B_prep = tomoself.get_pauli_basis(n)
    B_meas = tomoself.get_pauli_basis(n)
    
    lam = tomoself.get_lambda_from_meas(tomo_set,tomo_data['data'], n)
    
    A = tomoself.get_A_mat(B_prep,B_meas,B_chi)
    chivect = np.linalg.solve(A,lam)
    return np.reshape(chivect,((2*n)**2,(2*n)**2))


def plot(choi_matrix,method=None,message=None):
    if message != None:
        print(message+'\n')
    plot_state(choi_matrix,method)

def analyse(choi_matrix,choi_perfect, print_yes = None):
    fidelity = state_fidelity(vectorize(choi_perfect)/2, choi_matrix)
    difference = sum(sum(abs(choi_perfect-choi_matrix)))/(2**2)
    if print_yes == 'y':
        print('Process Fidelity = ', fidelity)
        print('Summed absolute difference = ', difference)
    
    return [fidelity, difference]

def matr_to_choi(matrix):
    choi = outer(vectorize(matrix))
    return choi

