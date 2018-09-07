# -*- coding: utf-8 -*-
"""
Created on Thu Aug 30 14:55:31 2018

@author: Jarnd
"""

#import sys
#sys.path.append('../')

import Functions.Data_storage as store
import Analysis.Analysis as an
from qiskit.tools.visualization import plot_state

run_type = 'r'
fit_method = 'magic'
circuit_name = 'FTSWAP'

timestamp = None;
direct = False

if direct == True:
    timestamp = store.load_last()['Experiment time']
    run_type = store.load_last()['Type']
results_loaded = store.load_results(circuit_name,run_type, timestamp)




#%%
tomo_set = results_loaded['Tomoset']


results = results_loaded['Results']
tomo_data = an.tomo.tomography_data(results,circuit_name,tomo_set)
choi_fit = an.fit_tomodata(tomo_data)

plot_state(choi_fit)