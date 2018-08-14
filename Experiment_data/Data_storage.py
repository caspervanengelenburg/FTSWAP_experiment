# -*- coding: utf-8 -*-
"""
Created on Mon Aug 13 15:13:38 2018

@author: Jarnd
"""
import pickle as pickle
import os as os

from datetime import datetime





def save_data(circuit_name,run_type,backend,tomo_data,nr_shots,notes=None):
    timenow = datetime.now()
    if run_type == 's':
        directory = 'Simulation_data/'
    elif run_type == 'r':
        directory = 'Real_data/'
    filepath = 'Experiment_data/'+directory+timenow.strftime("%m_%d-%H_%M_%S")+"--tomodata.txt"
    os.makedirs(os.path.dirname(filepath), exist_ok=True)
    data = {'Experiment time' : timenow , 'Circuit name' : circuit_name , 
            'Type' : run_type , 'Backend' : backend , 'Data' : tomo_data ,
            'Shot number' : nr_shots , 'Notes' : notes}
    pickle.dump(data, open(filepath, "wb"))
    return data

def load_data(run_type,timestamp=None):
    if run_type == 's':
        directory = 'Simulation data/'
    elif run_type == 'r':
        directory = 'Real data/'
    
    if timestamp == None:
        date = input('Date of experiment (mm_dd):')
        time = input('Time of experiment (hh_mm_ss):')
        filepath = directory+date+'-'+time+'--tomodata.txt'
        data_load = pickle.load(open(filepath,'rb'))
    elif type(timestamp) == datetime:
        filepath = directory+timestamp.strftime("%m_%d-%H_%M_%S")+"--tomodata.txt"
        data_load = pickle.load(open(filepath,"rb"))
    elif type(timestamp) == str:
        filepath = directory+timestamp+"--tomodata.txt"
        data_load = pickle.load(open(filepath,"rb"))   
    return data_load
        
