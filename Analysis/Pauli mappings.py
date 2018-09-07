# -*- coding: utf-8 -*-
"""
Created on Thu Sep  6 13:04:19 2018

@author: Jarnd
"""
import numpy as np
import itertools as itt

n = 2
def get_pauli_basis(n):
    I =    np.array([[1 , 0] , [0 , 1]])
    X =    np.array([[0 , 1] , [1 , 0]])
    Y = 1j*np.array([[0 , 1] , [-1, 0]])
    Z =    np.array([[1 , 0] , [0 ,-1]])
    P1 = [I,X,Y,Z]
    P2 = []
    for Bde in itt.product(P1,repeat = n):
        B = 1
        for i in Bde:
            B = np.kron(B,i)
        P2.append(B)
    return P2

def get_canonical_basis(n):
    E00 = np.array([[1 , 0] , [0 , 0]]);
    E01 = np.array([[0 , 1] , [0 , 0]]);
    E10 = np.array([[0 , 0] , [1 , 0]]);
    E11 = np.array([[0 , 0] , [0 , 1]]);
    E1 = [E00,E01,E10,E11]
    E2 = []
    for Bde in itt.product(E1,repeat = n):
        B = 1
        for i in Bde:
            B = np.kron(B,i)
        E2.append(B)
    return E2

P1names = ['I','X','Y','Z']


#%%
def get_Hilb_basis(n):
    basis = []
    for i in range(2**n):
        vect =  np.mat(np.zeros((2**n,1)))
        vect[i] = 1
        basis.append(vect)
    return basis

def get_max_ent_2n(n):
    n_bas = get_Hilb_basis(n)
    d = len(n_bas)
    for i in range(d):
        if i == 0:
            psi_ome = np.kron(n_bas[i],n_bas[i])
        else:
            psi_ome += np.kron(n_bas[i],n_bas[i])
    return psi_ome/np.sqrt(d)

#%%
def get_choi_basis(n):
    B_choi = []
    P_bas = get_pauli_basis(n)
    psi_ome = get_max_ent_2n(n)
    for P in P_bas:
        B_choi.append(np.kron(P,P_bas[0])@psi_ome)
    return B_choi
