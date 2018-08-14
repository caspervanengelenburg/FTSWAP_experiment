# -*- coding: utf-8 -*-
"""
Created on Tue Aug 14 15:59:14 2018

@author: Jarnd
"""

import getpass
try:
    #sys.path.append("../../") # go to parent dir
    import IBM_Q_Experience.Qconfig as Qconfig
    qx_config = {
        "APItoken": Qconfig.APItoken,
        "url": Qconfig.config['url']}
    print('Qconfig loaded from %s.' % Qconfig.__file__)
except:
    APItoken = getpass.getpass('Please input your token and hit enter: ')
    qx_config = {
        "APItoken": APItoken,
        "url":"https://quantumexperience.ng.bluemix.net/api"}
    print('Qconfig.py not found in qiskit-tutorial directory; Qconfig loaded using user input.')