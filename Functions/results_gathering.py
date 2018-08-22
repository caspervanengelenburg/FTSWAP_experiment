# -*- coding: utf-8 -*-
"""
Created on Wed Aug 22 17:35:02 2018

@author: Jarnd
"""

from IBMQuantumExperience import IBMQuantumExperience as IBMQ

from qiskit.backends.ibmq.ibmqjob import IBMQJob
import IBM_Q_Experience.Qconfig as Qconfig
api = IBMQ(Qconfig.APItoken, Qconfig.config)
import Functions.Data_storage as store

def get_results_from_jobids(jobids,run_type):
    if run_type == 's':
        chip = False
    elif run_type == 'r':
        chip = True
    nr_batches = len(jobids)
    for i in range(nr_batches):
        jobinfo = api.get_job(jobids[i])
        job = IBMQJob.from_api(jobinfo, api, chip)
        if not job.done:
            print('Job with batchnr %d/%d not done yet (id=%s )\n' %(i+1,nr_batches,jobids[i]))
            results = None
            break
        if i == 0:
            results = job.result()
        else:
            results += job.result()
    return results

def get_tomoset_from_file(direct, circuit_name = None, run_type = None, timestamp = None):
    if direct == True:
        loaded_jobiddata = store.load_last()
    elif direct == False:
        if circuit_name == None:
            circuit_name = input('Circuit name: ')
        if run_type == None:
            run_type = input('Run Type: ')
        if timestamp == None:
            date = input('Date of experiment (mm_dd):')
            time = input('Time of experiment (hh_mm_ss):')
            loaded_jobiddata = store.load_jobids(circuit_name, run_type,date+'-'+time)
        else:
            loaded_jobiddata = store.load_jobids(circuit_name, run_type,timestamp)
    return loaded_jobiddata['tomoset']
    
def get_jobids_from_file(direct, circuit_name = None, run_type = None, timestamp = None):
    if direct == True:
        loaded_jobiddata = store.load_last()
    elif direct == False:
        if circuit_name == None:
            circuit_name = input('Circuit name: ')
        if run_type == None:
            run_type = input('Run Type: ')
        if timestamp == None:
            date = input('Date of experiment (mm_dd):')
            time = input('Time of experiment (hh_mm_ss):')
            loaded_jobiddata = store.load_jobids(circuit_name, run_type,date+'-'+time)
        else:
            loaded_jobiddata = store.load_jobids(circuit_name, run_type,timestamp)   
    nr_batches = loaded_jobiddata['Batchnumber'];
    jobids = ['']*nr_batches
    for job in loaded_jobiddata['Data']:
        jobids[job['batchno']] = job['Jobid']
    return [jobids, loaded_jobiddata['Tomoset']]

