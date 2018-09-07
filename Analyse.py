# -*- coding: utf-8 -*-
"""
Created on Wed Aug 15 08:59:49 2018

@author: Jarnd
"""

import Analysis.Analysis as an
import Functions.results_gathering as rg
from qiskit.tools.visualization import plot_state
from qiskit import register, unregister, get_backend


#%%
from IBM_Q_Experience.Q_Exp_register import qx_config
provider = register(qx_config['APItoken'])

#%%

direct = True
run_type = 's'

if run_type == 's':
    backend = get_backend('ibmq_qasm_simulator')
elif run_type == 'r':
    backend = get_backend('ibmqx4')
#%%


fit_method = 'leastsq'
circuit_name = 'FTSWAP'

if direct:
    run_type = rg.store.load_last()['Type']


[jobids, jobdata] = rg.get_jobids_from_file(direct,circuit_name,run_type)
stati = rg.get_status_from_jobids(jobids,printing=True)
tomo_set = jobdata['Tomoset']

if 'RUNNING' not in stati:
    results = rg.get_results_from_jobids(jobids,backend)
    calibrations = rg.get_calibration_from_jobids(jobids)
    rg.store.save_results(circuit_name, jobdata['Experiment time'],jobdata['Type'],jobdata['Backend'],jobids,
                          tomo_set,jobdata['Batchnumber'],jobdata['Shot number'],results, calibrations, notes=None)
    tomo_data = an.tomo.tomography_data(results,circuit_name,tomo_set)
    choi_fit = an.fit_tomodata(tomo_data)

    plot_state(choi_fit)


#%%
unregister(provider)