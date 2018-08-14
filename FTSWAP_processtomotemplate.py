# -*- coding: utf-8 -*-
"""
Created on Fri Aug  3 15:01:21 2018

@author: Jarnd
"""

# importing the QISKit
from qiskit import register




# useful additional packages 
import Analysis.Analysis as an
import Experiment_data.Data_storage as store
import Functions.Create_tomo_circuits as tomo

###############################################################################
# Simulation or real experimemt? 's' for simulation, 'r' for real
run_type = 's'
reg = True #Set to true to register at IBM

notes = ''#Optional notes to be stored in the datafile
maximum_credits = 8
anal_true = True
plot_true = True

###############################################################################
# Register at IBM Quantum Experience using token
if reg == True:
    
    from IBM_Q_Experience.Q_Exp_register import qx_config
    register(qx_config['APItoken'])

# Import Quantum program of desired circuit
from Circuits.circuit_FTSWAP import Q_program, q, c
circuit_name = Q_program.get_circuit_names()[0]

###############################################################################
# Set number of shots, timeout, measurement- and preperation basis and backend
shots = 200
timeout = 50
backendsim = 'local_qasm_simulator'
backendreal = 'ibmqx4'
meas_basis, prep_basis = 'Pauli', 'Pauli'


if run_type == 's':
    backend = backendsim
elif run_type == 'r':
    backend = backendreal
else: print('Error, wrong runtype!')
################################################################################
# Create tomo set and tomo circuits; put them in the quantum program
[Q_program,tomo_set,tomo_circuits] = tomo.create_tomo_circuits(Q_program,circuit_name,q,c,[1,0],meas_basis,prep_basis)



# Execute all the tomo circuits
results = Q_program.execute(tomo_circuits, shots=shots, backend=backend,timeout=timeout,max_credits = maximum_credits)

###############################################################################
# Gather data from the results & save to specific folder
results_data = tomo.extract_data(results,circuit_name,tomo_set)

store.save_data(circuit_name,run_type,backend,results_data,shots,notes)


###############################################################################
if anal_true == True:
    
    choi_fit = an.fit_tomodata(results_data,'leastsq')
    if plot_true == True:
        
        an.plot(choi_fit)