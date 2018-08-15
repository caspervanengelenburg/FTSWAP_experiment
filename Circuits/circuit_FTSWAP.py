# -*- coding: utf-8 -*-
"""
Created on Tue Aug 14 16:02:12 2018

@author: Jarnd
"""
from qiskit import QuantumProgram
# Creating registers
Q_program = QuantumProgram()

# Creating registers
q = Q_program.create_quantum_register("qr", 3)
c = Q_program.create_classical_register("cr", 3)

qc = Q_program.create_circuit("FTSWAP",[q],[c])


###############################################################################
#Specify FT SWAP circuit

# Swap gate between qubit 0 and 2 as 3 CX's
# CX from qubit 2 to qubit 0
qc.cx(q[2], q[0]) 
# CX from qubit 0 to qubit 2 is not possible, flip using hadamards
qc.h(q[0])
qc.h(q[2])
qc.cx(q[2], q[0])
qc.h(q[0])
qc.h(q[2])
# CX from qubit 2 to qubit 0
qc.cx(q[2], q[0])


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

# Swap gate between qubit 1 and 2 as 3 CX's
# CX from qubit 2 to qubit 1
qc.cx(q[2], q[1]) 
# CX from qubit 1 to qubit 2 is not possible, flip using hadamards
qc.h(q[1])
qc.h(q[2])
qc.cx(q[2], q[1])
qc.h(q[1])
qc.h(q[2])
# CX from qubit 2 to qubit 1
qc.cx(q[2], q[1])

###############################################################################
# Define 