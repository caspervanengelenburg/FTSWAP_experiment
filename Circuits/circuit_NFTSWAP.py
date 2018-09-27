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

qc = Q_program.create_circuit("NFTSWAP",[q],[c])


###############################################################################
#Specify NFT SWAP circuit


# Swap gate between qubit 0 and 1 as 3 CX's
# CX from qubit 1 to qubit 0
qc.cx(q[1], q[0]) 
# CX from qubit 0 to qubit 1 is not possible, flip using hadamards
qc.h(q[0])
qc.h(q[1])
qc.cx(q[1], q[0])
qc.h(q[0])
qc.h(q[1])
# CX from qubit 1 to qubit 0
qc.cx(q[1], q[0])


###############################################################################
# Define perfect Unitary
Unitary = np.array([[1, 0, 0, 0],[0, 0, 1, 0],[0, 1, 0, 0],[0, 0, 0, 1]])