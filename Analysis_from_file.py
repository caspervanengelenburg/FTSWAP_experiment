# -*- coding: utf-8 -*-
"""
Created on Thu Aug 30 14:55:31 2018

@author: Jarnd
"""

#import sys
#sys.path.append('../')

import Functions.results_gathering as rg
import Functions.Data_storage as store

run_type = 'r'
fit_method = 'leastsq'
circuit_name = 'FTSWAP'

timestamp = None;
direct = False

if direct == True:
    timestamp = store.load_last()['Experiment time']
    run_type = store.load_last()['Type']
results_loaded = store.load_results(circuit_name,run_type, timestamp)





#
#stati = rg.get_status_from_jobids(jobids,printing=True)
#tomo_set = jobdata['Tomoset']
#
#if 'RUNNING' not in stati:
#    results = rg.get_results_from_jobids(jobids,run_type)
#    rg.store.save_results(circuit_name, jobdata['Experiment time'],jobdata['Type'],jobdata['Backend'],jobids,
#                          tomo_set,jobdata['Batchnumber'],jobdata['Shot number'],results, notes=None)
#    tomo_data = an.tomo.tomography_data(results,circuit_name,tomo_set)
#    choi_fit = an.fit_tomodata(tomo_data)
#
#    plot_state(choi_fit)