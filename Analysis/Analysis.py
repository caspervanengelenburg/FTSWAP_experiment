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
#from Functions.Create_tomo_circuits import *

def fit_tomodata(tomo_data,method=None):
    if method == 'Linear inversion':
        print('Error, no method yet!')
        choi_fit = []
    elif method == None:
        choi_fit = tomo.fit_tomography_data(tomo_data,options={'trace':1})
    else: 
        choi_fit = tomo.fit_tomography_data(tomo_data,method,options={'trace':1})
    return choi_fit

def fit_chi_own(tomo_data,tomo_set, n):
    B_chi = tomoself.get_pauli_basis(n)
    B_prep = tomoself.get_pauli_basis_unnorm(n)
    B_meas = tomoself.get_pauli_basis_unnorm(n)
    
    lam, lampau = tomoself.get_lambda_from_meas(tomo_set,tomo_data['data'], n)
    
    A = tomoself.get_A_mat(B_prep,B_meas,B_chi)
    chivect = np.linalg.solve(A,lam)
    return np.reshape(chivect,((2*n)**2,(2*n)**2))

def get_total_prob(tomo_data):
    meas_data = tomo_data['data'] 
    counts = []
    for meas in meas_data:
        countsvalues = meas['counts'].values()
        counts.append(sum(list(countsvalues))/meas['shots'])
    return counts

def make_CP(chi,n):
    mineig = np.min(np.linalg.eigvals(chi))
    trace_chi = np.trace(chi)
    if mineig < 0:    
        chiCP = np.add(chi,(-1)*mineig*np.eye((2*n)**2))
    return trace_chi*chiCP/np.trace(chiCP)

def check_TP(chi,B_chi):
    d2 = np.shape(chi)[0]
    iden = np.zeros_like(B_chi[0],dtype='complex')
    for m in range(d2):
        for n in range(d2):
            iden += chi[m,n]*np.mat(B_chi[n]).H@np.mat(B_chi[m])
    return iden

def get_chi_error(chi, chi_bas, U, mode = 'p'):
    chi = np.mat(chi)
    U = np.mat(U)
    V = np.mat(np.zeros((len(chi_bas),len(chi_bas))),dtype='complex')
    mc = 0;
    for i in range(len(chi_bas)):
        chi_bas[i] = np.mat(chi_bas[i])
    for m in chi_bas:
        nc = 0;
        for n in chi_bas:
            if mode == 'p':
                V[mc,nc] = np.trace(m.H @ n @ U.H)
            if mode == 'n':
                V[mc,nc] = np.trace(m.H @ U.H @ n)
            nc += 1;
        mc += 1
    return V @ chi @ V.H


def unit_to_choi(Unitary):
    choi = outer(vectorize(Unitary))
    return choi

