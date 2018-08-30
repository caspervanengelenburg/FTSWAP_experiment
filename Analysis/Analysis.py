# -*- coding: utf-8 -*-
"""
Created on Tue Aug 14 15:22:48 2018

@author: Jarnd
"""
import qiskit.tools.qcvv.tomography as tomo
from qiskit.tools.qi.qi import outer, vectorize, state_fidelity
from qiskit.tools.visualization import plot_state
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

