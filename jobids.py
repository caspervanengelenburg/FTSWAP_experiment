# -*- coding: utf-8 -*-
"""
Created on Sat Aug 25 17:33:49 2018

@author: jarnd
"""

import Functions.results_gathering as rg
import pickle

running_jobsdata = []
running_jobs = []


last_jobs = rg.get_last_jobids_and_data(nr= 200, only_real=True)
for job in last_jobs:
    if job[2]  == 'RUNNING':
        running_jobsdata.append(job)
        running_jobs.append(job[0])

data = {'jobids_all':last_jobs,'jobidsdata_running':running_jobsdata,'jobids_running':running_jobs}

fp = 'jobids_data.pickle'
fh = open(fp,'wb')
pickle.dump(data, fh)
fh.close
fp = 'jobids_data.txt'
fh = open(fp,'w')
for id in running_jobs:
    str = id+'\n'
    fh.write(str)
fh.close()

