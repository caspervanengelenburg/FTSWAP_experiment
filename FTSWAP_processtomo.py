# -*- coding: utf-8 -*-
"""
Created on Fri Aug  3 15:01:21 2018

@author: Jarnd
"""


"""
This code was inspired/based on the qiskit tutorials provided by IBM, available
at the qiskit-tutorials github. The Q_Exp_register file especially is based on 
the 'process_tomography.py' file.
"""

# importing the QISKit
from qiskit import register, execute, get_backend




# useful additional packages 
import Functions.Data_storage as store
import Functions.Create_tomo_circuits as tomo

###############################################################################
# Simulation or real experimemt? 's' for simulation, 'r' for real
run_type = 'r'
reg = True #Set to true to register at IBM

notes = ''#Optional notes to be stored in the datafile
maximum_credits = 8; # Maximum number of credits


nr_batches = 6; # Tries 6 batches, if total number of circuits is not divisible adds one extra batch with the leftovers


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
shots = 200 # #shots for every circuit
#timeout = 500000 # timeout in seconds before execution halts. This is the per-batch timeout, so total runtime <500*(nr_batches+1) seconds
backendsim = 'ibmq_qasm_simulator' # The backend to use in the simulations. Check available_backends() for all backends
backendreal = 'ibmqx4' # The backed to use for the actual experiments (e.g. the chip)
meas_basis, prep_basis = 'Pauli', 'Pauli' # Measurement and preparation basis for process tomography

# Set backend based on run_type
if run_type == 's':
    backendname = backendsim
elif run_type == 'r':
    backendname = backendreal
else: print('Error, wrong runtype!')

ibmqxbackend = get_backend(backendreal)
jobs = []
job_data = []
################################################################################
# Create tomo set and tomo circuits; put them in the quantum program
[Q_program,tomo_set,tomo_circuits] = tomo.create_tomo_circuits(Q_program, circuit_name,q,c,[1,0],meas_basis,prep_basis)



# Execute all the tomo circuits
batch_size = int(len(tomo_circuits)/nr_batches);
if len(tomo_circuits)%nr_batches != 0:
    nr_batches +=1
    
for i in range(nr_batches):
    run_circuits = tomo_circuits[i*batch_size:(i+1)*batch_size]
    circuit_list = []
    for cir in run_circuits:
        Q_program.get_circuit(cir).name = cir
        circuit_list.append(Q_program.get_circuit(cir))
    print('Batch %d/%d: %s' % (i+1, nr_batches, 'INITIALIZING'))
    if i==0:
        job = execute(circuit_list, backend=backendname, shots=shots)
        jobs.append(job)
        job_data.append({'Date':job.creation_date,'Jobid':job.id,'runtype':run_type,'batchno':i})
        print('Batch %d/%d: %s' % (i+1, nr_batches, 'SENT'))
    else:
        job = execute(circuit_list, backend=backendname, shots=shots)
        jobs.append(job)
        job_data.append({'Date':job.creation_date,'Jobid':job.id,'runtype':run_type,'batchno':i})
        print('Batch %d/%d: %s' % (i+1, nr_batches, 'SENT'))

###############################################################################
store.save_jobids(circuit_name,job_data,tomo_set,backendname,shots,nr_batches,run_type)
store.save_last(circuit_name,job_data,tomo_set,backendname,shots,nr_batches,run_type)