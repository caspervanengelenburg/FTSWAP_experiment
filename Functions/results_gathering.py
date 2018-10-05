# -*- coding: utf-8 -*-
"""
Created on Wed Aug 22 17:35:02 2018

@author: Jarnd
"""

from IBMQuantumExperience import IBMQuantumExperience as IBMQ

import IBM_Q_Experience.Qconfig as Qconfig
api = IBMQ(Qconfig.APItoken, Qconfig.config)
import Functions.Data_storage as store


def get_results_from_jobids(jobids, backend):
    nr_batches = len(jobids)
    for i in range(nr_batches):
        job = backend.retrieve_job(jobids[i])
        if not job.done:
            print('Job with batchnr %d/%d not done yet (id=%s )\n' %
                  (i+1, nr_batches, jobids[i]))
            results = None
            break
        if i == 0:
            results = job.result()
        else:
            results += job.result()
    return results


def get_calibration_from_jobids(jobids):
    nr_batches = len(jobids)
    calibrations = [None]*nr_batches
    for i in range(nr_batches):
        jobinfo = api.get_job(jobids[i])
        if not jobinfo['status'] == 'COMPLETED':
            print('Job with batchnr %d/%d not done yet (id=%s )\n' %
                  (i+1, nr_batches, jobids[i]))
            calibrations = None
            break
        calibrations[i] = jobinfo['calibration']
    return calibrations


def cancel_jobs_from_jobids(jobids, backend):
    nr_batches = len(jobids)
    for i in range(nr_batches):
        job = backend.retrieve_job(jobids[i])
        if job.done:
            print('Job with id=%s already done)\n' % (jobids[i]))
            continue
        jobcancel = job.cancel()
        if jobcancel:
            print('Job with id=%s has been cancelled)\n' % (jobids[i]))
        if not jobcancel:
            print('Job with id=%s cannot be cancelled)\n' % (jobids[i]))


def get_tomoset_from_file(direct, circuit_name=None, run_type=None, timestamp=None):
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
            loaded_jobiddata = store.load_jobdata(
                circuit_name, run_type, date+'-'+time)
        else:
            loaded_jobiddata = store.load_jobdata(
                circuit_name, run_type, timestamp)
    return loaded_jobiddata['tomoset']


def get_jobids_from_file(direct, circuit_name=None, run_type=None, timestamp=None):
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
            loaded_jobiddata = store.load_jobdata(
                circuit_name, run_type, date+'-'+time)
        else:
            loaded_jobiddata = store.load_jobdata(
                circuit_name, run_type, timestamp)
    nr_batches = loaded_jobiddata['Batchnumber']
    jobids = ['']*nr_batches
    for job in loaded_jobiddata['Data']:
        jobids[job['batchno']] = job['Jobid']
    return [jobids, loaded_jobiddata]


def get_last_jobids_and_data(nr=1, dates=True, status=True, only_real=False):
    data = []
    jobs = api.get_jobs(nr)
    for i in range(len(jobs)):
        if only_real:
            if jobs[i]['backend']['name'] != 'ibmqx4':
                continue
        entry = [jobs[i]['id']]
        if dates == True:
            entry.append(jobs[i]['creationDate'])
        if status == True:
            entry.append(jobs[i]['status'])
        data.append(entry)
    return data


def get_last_jobids(nr=1, only_real=False):
    data = []
    jobs = api.get_jobs(nr)
    for i in range(len(jobs)):
        if only_real:
            if jobs[i]['backend']['name'] != 'ibmqx4':
                continue
        data.append(jobs[i]['id'])
    return data


def get_status_from_jobids(jobids, printing=False):
    job_stati = []
    jobnr = 1
    totalnr = len(jobids)
    for jobid in jobids:
        jobstatus = api.get_job(jobid)['status']
        if printing == True:
            print('Job nr %d/%d status: %s' % (jobnr, totalnr, jobstatus))
        job_stati.append(jobstatus)
        jobnr += 1
    return job_stati
