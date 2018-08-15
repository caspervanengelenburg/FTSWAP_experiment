# -*- coding: utf-8 -*-
"""
Created on Wed Aug 15 08:59:49 2018

@author: Jarnd
"""

import Analysis.Analysis as an
import Experiment_data.Data_storage as store

direct = True
run_type = 's'

fit_method = 'leastsq'

if direct == True:
    loaded_data = store.load_data(circuit_name,run_type,timestamp)
elif direct == False:
    date = input('Date of experiment (mm_dd):')
    time = input('Time of experiment (hh_mm_ss):')
    circuit = input('Name of experinent circuit:')
    loaded_data = store.load_data(circuit,run_type,date+'-'+time)

loaded_tomo_data = loaded_data['Data'];

an.fit_tomodata(loaded_tomo_data, method=fit_method);
