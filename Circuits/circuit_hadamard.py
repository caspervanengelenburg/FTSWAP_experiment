# -*- coding: utf-8 -*-
"""
Created on Wed Aug 22 11:57:56 2018

@author: Jarnd
"""

from qiskit import QuantumProgram
# Creating program
Q_program = QuantumProgram()

# Creating registers
q = Q_program.create_quantum_register("qr", 1)
c = Q_program.create_classical_register("cr", 1)

qc = Q_program.create_circuit("Hadamard",[q],[c])

###############################################################################
#Specify Hadamard circuit

qc.h(q[0])