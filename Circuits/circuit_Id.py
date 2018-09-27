# -*- coding: utf-8 -*-
"""
Created on Tue Aug 14 16:02:12 2018

@author: Jarnd
"""
from qiskit import QuantumProgram
import numpy as np
# Creating program
Q_program = QuantumProgram()

# Creating registers
q = Q_program.create_quantum_register("qr", 3)
c = Q_program.create_classical_register("cr", 3)

qc = Q_program.create_circuit("Id",[q],[c])


###############################################################################
#Specify FT SWAP circuit
qc.iden(q[0])
qc.iden(q[1])
###############################################################################
# Define perfect Unitary
Unitary = np.array([[1, 0, 0, 0],[0, 1, 0, 0],[0, 0, 1, 0],[0, 0, 0, 1]])