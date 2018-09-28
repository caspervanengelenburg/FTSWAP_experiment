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
import Functions.Plotting as pt
import numpy as np


fit_method = 'own'
n = 2;


direct = False

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

#%% Tomography; 
B_chi = tomoself.get_pauli_basis(n)
B_choi = tomoself.get_choi_basis(n, B_chi)

if fit_method == 'wizard':
    # Fitting choi with qiskit functions 'wizard' method and mapping choi to chi
    choi = an.fit_tomodata(tomo_data, method='wizard')
    chi = tomoself.choi_to_chi(choi,B_choi,n)
elif fit_method == 'leastsq':
    # Fitting choi with qiskit functions 'leastsq' method and mapping choi to chi
    choi = an.fit_tomodata(tomo_data, method='leastsq')
    choi = an.make_CP(choi,n)
    chi = tomoself.choi_to_chi(choi,B_choi,n)
elif fit_method == 'own':
    # Fitting choi with own functions and mapping chi
    chi = an.fit_chi_own(tomo_data,tomo_set, n)
    chi = an.make_CP(chi,n)
    choi = an.tomoself.chi_to_choi(chi,B_choi,n)



#%% Filter meas errors out
Bfilter = store.load_chi_meas_last()['B_filter']
chi_filtered = an.filter_chi_meas(chi,Bfilter,n)
choi_filtered = tomoself.chi_to_choi(chi_filtered,B_choi,n)

#%% Calculate error matrices
chi_perror = an.get_chi_error(chi_filtered,B_chi,results_loaded['Unitary'])
#chi_perror_before_filter = an.get_chi_error(chi, B_chi, results_loaded['Unitary'])
print('Tp:', an.check_TP(chi_filtered,B_chi,n))

#%% Calculated traces and fidelities
process_fidelity = chi_perror[0,0]/(2**n)
channel_fidelity = tomoself.get_max_ent_2n(n).T @ choi_filtered @ tomoself.get_max_ent_2n(n)

print('Trace of filtered Chi:',np.trace(chi_filtered))
print('Trace of filtered Choi:',np.trace(choi_filtered))
print('Trace of error Chi :',np.trace(chi_perror))

print('Process fidelity from error matrix:',np.abs(process_fidelity))
print('Channel fidelity from Choi matrix:',np.float(np.abs(channel_fidelity)))

#%% Plotting
pt.plot_city(chi_filtered,tomoself.get_pauli_names(n)) 
pt.plot_city(chi_perror,tomoself.get_pauli_names(n))