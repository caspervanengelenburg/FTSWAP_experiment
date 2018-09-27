# -*- coding: utf-8 -*-
"""
Created on Thu Aug 30 14:55:31 2018

@author: Jarnd
"""

#import sys
#sys.path.append('../')

import Functions.Data_storage as store
import Analysis.Analysis as an
import Analysis.tomography_functions as tomoself
from qiskit.tools.visualization import plot_state
import Functions.Plotting as pt
import numpy as np


fit_method = None
n = 2;


direct = True

#%% Gather the results from file
if direct == True:
    timestamp = store.load_last()['Experiment time']
    run_type = store.load_last()['Type']
    circuit_name = store.load_last()['Circuit name']
else:
    run_type = input('Run Type is (enter as string): ')
    circuit_name = input('Circuit name is(enter as string): ')
    timestamp = None;
results_loaded = store.load_results(circuit_name, run_type, timestamp)




#%% Gather the tomo set and its outcomes from the results
tomo_set = results_loaded['Tomoset']
results = results_loaded['Results']
tomo_data = an.tomo.tomography_data(results,circuit_name,tomo_set)

#%% Tomography; fitting choi with qiskit functions and mapping choi to chi
choi_qiskitfit = an.fit_tomodata(tomo_data,method = fit_method)
choi_qiskitfit = an.make_CP(choi_qiskitfit,n)

B_chi = tomoself.get_pauli_basis(n)
B_choi = tomoself.get_choi_basis(n, B_chi)
chi_qiskitfit = tomoself.choi_to_chi(choi_qiskitfit,B_choi,n)

#%% Tomography; fitting chi with own functions
chi_ownfit = an.fit_chi_own(tomo_data,tomo_set, n)
chi_ownfit = an.make_CP(chi_ownfit,n)
choi_ownfit = tomoself.chi_to_choi(chi_ownfit, B_choi,n)


#%%



#%% Plotting
#plot_state(chi_qiskitfit)
#plot_state(chi_ownfit)
pt.plot_city(chi_ownfit,tomoself.get_pauli_names(n)) 
#%% Calculated traces
print('Trace of Chi qiskit fit:',np.trace(chi_qiskitfit))
print('Trace of Chi own fit:',np.trace(chi_ownfit))
print('Trace of Choi qiskit fit:',np.trace(choi_qiskitfit))
print('Trace of Choi own fit:',np.trace(choi_ownfit))

#%% Analysis
chi_perror_ownfit = an.get_chi_error(chi_ownfit,B_chi,results_loaded['Unitary'])
channel_fidelity_ownfit = chi_perror_ownfit[0,0]/4
channel_fidelity_ownfit_Ben = (2*n)*tomoself.get_max_ent_2n(n).T @ choi_ownfit @ tomoself.get_max_ent_2n(n)
#plot_state(chi_perror)
iden = an.check_TP(chi_ownfit,B_chi)
print('Process fidelity from error matrix:',np.abs(channel_fidelity_ownfit))
print('Process fidelity from Choi matrix:',np.float(np.abs(channel_fidelity_ownfit_Ben)))

