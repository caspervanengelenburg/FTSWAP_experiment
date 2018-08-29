# -*- coding: utf-8 -*-
"""
Created on Mon Aug 13 15:13:38 2018

@author: Jarnd
"""
import pickle as pickle
import os as os

from datetime import datetime





def save_tomo_data(circuit_name,run_type,backend,tomo_data,nr_shots,notes=None):
    timenow = datetime.now()
    if run_type == 's':
        directory = 'Experiment_data/Simulation_data/'
    elif run_type == 'r':
        directory = 'Experiment_data/Real_data/'
    filepath = directory+circuit_name+'--'+timenow.strftime("%m_%d-%H_%M_%S")+"--tomodata.txt"
    os.makedirs(os.path.dirname(filepath), exist_ok=True)
    data = {'Experiment time' : timenow , 'Circuit name' : circuit_name , 
            'Type' : run_type , 'Backend' : backend , 'Data' : tomo_data ,
            'Shot number' : nr_shots , 'Notes' : notes}
    pickle.dump(data, open(filepath, "wb"))
    return data

def load_tomo_data(circuit_name,run_type,timestamp=None):
    if run_type == 's':
        directory = 'Experiment_data/Simulation_data/'
    elif run_type == 'r':
        directory = 'Experiment_data/Real_data/'
    
    if timestamp == None:
        date = input('Date of experiment (mm_dd):')
        time = input('Time of experiment (hh_mm_ss):')
        filepath = directory+circuit_name+'--'+date+'-'+time+'--tomodata.txt'
        data_load = pickle.load(open(filepath,'rb'))
    elif type(timestamp) == datetime:
        filepath = directory+circuit_name+'--'+timestamp.strftime("%m_%d-%H_%M_%S")+"--tomodata.txt"
        data_load = pickle.load(open(filepath,"rb"))
    elif type(timestamp) == str:
        filepath = directory+circuit_name+'--'+timestamp+"--tomodata.txt"
        data_load = pickle.load(open(filepath,"rb"))   
    return data_load
        
def save_jobdata(circuit_name,jobs_data,tomo_set,backend,nr_shots,nr_batches,run_type, notes=None):
    timenow = datetime.now()
    if run_type == 's':
        directory = 'Experiment_data/Simulation_data/'
    elif run_type == 'r':
        directory = 'Experiment_data/Real_data/'    
    filepathtxt = directory+circuit_name+'/'+circuit_name+'--'+timenow.strftime("%m_%d-%H_%M_%S")+"--jobdata.txt"
    filepathpickle = directory+circuit_name+'/'+circuit_name+'--'+timenow.strftime("%m_%d-%H_%M_%S")+"--jobdata.pickle"
    os.makedirs(os.path.dirname(filepathtxt), exist_ok=True)
    fo = open(filepathtxt,'w')
    fo.write('Job id\'s for experiment ran on '+jobs_data[0]['Date']+'\n')
    fo.write('Data saved on '+timenow.strftime("%m_%d-%H_%M_%S")+'\n')
    if run_type == 's':
        exptype = 'simulation'
    elif run_type == 'r':
        exptype = 'real'
    fo.write('Experiment type is '+exptype+'\n')
    fo.write('Number of batches is '+str(nr_batches)+'\n\n')
    for job in jobs_data:
        fo.write('Job nr %d/%d: \n'% (job['batchno']+1,nr_batches))
        fo.write('Date: '+job['Date']+'\n')
        fo.write('Job id:\n'+job['Jobid']+'\n\n')
    fo.close()
    datadict = {'Experiment time' : timenow , 'Circuit name' : circuit_name , 
            'Type' : run_type , 'Backend' : backend , 'Data' : jobs_data , 
            'Tomoset' : tomo_set , 'Shot number' : nr_shots , 
            'Batchnumber' : nr_batches , 'Notes' : notes}
    fo = open(filepathpickle, 'wb')
    pickle.dump(datadict, fo)
    fo.close


    
def load_jobids(circuit_name, run_type, timestamp=None):
    if run_type == 's':
        directory = 'Experiment_data/Simulation_data/'
    elif run_type == 'r':
        directory = 'Experiment_data/Real_data/'
    
    if timestamp == None:
        date = input('Date of experiment (mm_dd):')
        time = input('Time of experiment (hh_mm_ss):')
        filepath = directory+circuit_name+'/'+circuit_name+'--'+date+'-'+time+'--jobdata.pickle'
        data_load = pickle.load(open(filepath,'rb'))
    elif type(timestamp) == datetime:
        filepath = directory+circuit_name+'/'+circuit_name+'--'+timestamp.strftime("%m_%d-%H_%M_%S")+"--jobdata.pickle"
        data_load = pickle.load(open(filepath,"rb"))
    elif type(timestamp) == str:
        filepath = directory+circuit_name+'/'+circuit_name+'--'+timestamp+"--jobdata.pickle"
        data_load = pickle.load(open(filepath,"rb"))   
    return data_load

def save_last(circuit_name,data,tomo_set,backend,nr_shots,nr_batches,run_type, notes=None):
    timenow = datetime.now()  
    filepathpickle = "Experiment_data/last--jobdata.pickle"
    os.makedirs(os.path.dirname(filepathpickle), exist_ok=True)
    datadict = {'Experiment time' : timenow , 'Circuit name' : circuit_name , 
            'Type' : run_type , 'Backend' : backend , 'Data' : data , 
            'Tomoset' : tomo_set , 'Shot number' : nr_shots , 
            'Batchnumber' : nr_batches , 'Notes' : notes}
    fo = open(filepathpickle, 'wb')
    pickle.dump(datadict, fo)
    fo.close

def load_last():    
    filepathpickle = "Experiment_data/last--jobdata.pickle"
    data_load = pickle.load(open(filepathpickle, 'rb'))
    return data_load
    

def save_results(circuit_name, timestamp,run_type,backend, jobids, tomo_set, nr_batches,nr_shots,results, notes=None):
    if run_type == 's':
        directory = 'Experiment_data/Simulation_data/'
    elif run_type == 'r':
        directory = 'Experiment_data/Real_data/'    
    
    filepathpickle = directory+circuit_name+'/'+circuit_name+'--'+timestamp.strftime("%m_%d-%H_%M_%S")+"--results.pickle"
    os.makedirs(os.path.dirname(filepathpickle), exist_ok=True)

    datadict = {'Experiment time' : timestamp , 'Circuit name' : circuit_name , 
            'Type' : run_type , 'Backend' : backend , 'results' : results, 
            'Tomoset' : tomo_set , 'Shot number' : nr_shots , 'Jobids' : jobids,
            'Batchnumber' : nr_batches , 'Notes' : notes}
    fo = open(filepathpickle, 'wb')
    pickle.dump(datadict, fo)
    fo.close

def load_jobdata(circuit_name,run_type,timestamp=None):
    if run_type == 's':
        directory = 'Experiment_data/Simulation_data/'
    elif run_type == 'r':
        directory = 'Experiment_data/Real_data/'
    
    if timestamp == None:
        date = input('Date of experiment (mm_dd):')
        time = input('Time of experiment (hh_mm_ss):')
        filepath = directory+circuit_name+'--'+date+'-'+time+'--tomodata.txt'
        data_load = pickle.load(open(filepath,'rb'))
    elif type(timestamp) == datetime:
        filepath = directory+circuit_name+'--'+timestamp.strftime("%m_%d-%H_%M_%S")+"--tomodata.txt"
        data_load = pickle.load(open(filepath,"rb"))
    elif type(timestamp) == str:
        filepath = directory+circuit_name+'--'+timestamp+"--tomodata.txt"
        data_load = pickle.load(open(filepath,"rb"))   
    return data_load