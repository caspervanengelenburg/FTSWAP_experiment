# -*- coding: utf-8 -*-
"""
Created on Wed Aug 15 08:59:49 2018

@author: Jarnd
"""

import Analysis.Analysis as an
import Functions.results_gathering as rg
from qiskit.tools.visualization import plot_state

direct = True
run_type = 'r'

fit_method = 'leastsq'
circuit_name = 'Hadamard'






[jobids, tomo_set] = rg.get_jobids_from_file(direct,circuit_name,run_type)
stati = rg.get_status_from_jobids(jobids,printing=True)


if 'RUNNING' not in stati:
    results = rg.get_results_from_jobids(jobids,run_type)

    tomo_data = an.tomo.tomography_data(results,circuit_name,tomo_set)
    choi_fit = an.fit_tomodata(tomo_data)

    plot_state(choi_fit)
