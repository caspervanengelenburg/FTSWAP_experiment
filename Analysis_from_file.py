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

run_type = 's'
fit_method = 'leastsq'
circuit_name = 'FTSWAP'
n = 2;

timestamp = None;
direct = False

#%% Gather the results from file
if direct == True:
    timestamp = store.load_last()['Experiment time']
    run_type = store.load_last()['Type']
results_loaded = store.load_results(circuit_name, run_type, timestamp)




#%% Gather the tomo set and its outcomes from the results
tomo_set = results_loaded['Tomoset']


results = results_loaded['Results']
tomo_data = an.tomo.tomography_data(results,circuit_name,tomo_set)


#%% Tomography; fitting chi with own functions
chi_ownfit = an.fit_chi_own(tomo_data,tomo_set, n)

#%% Tomography; fitting choi with qiskit functions and mapping choi to chi
choi_qiskitfit = an.fit_tomodata(tomo_data,method = fit_method)

B_chi = tomoself.get_pauli_basis(n)
B_choi = tomoself.get_choi_basis(n, B_chi)
chi_qiskitfit = tomoself.choi_to_chi(choi_qiskitfit,B_choi,n)

#%% Plotting
plot_state(chi_qiskitfit)
plot_state(chi_ownfit)
