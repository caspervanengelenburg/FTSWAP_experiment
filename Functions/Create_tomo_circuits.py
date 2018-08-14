# -*- coding: utf-8 -*-
"""
Created on Tue Aug 14 16:19:11 2018

@author: Jarnd
"""

# import tomography libary
import qiskit.tools.qcvv.tomography as tomo


def create_tomo_circuits(Quantum_program,
                         circuit_name,
                         quantum_register,
                         classical_register,
                         qubit_list,
                         meas_basis='Pauli',
                         prep_basis='Pauli'):
    # Create tomo set and tomo circuits; put them in the quantum program
    tomo_set = tomo.process_tomography_set(qubit_list,meas_basis,prep_basis)
    tomo_circuits = tomo.create_tomography_circuits(Quantum_program,
                                                    circuit_name,
                                                    quantum_register,
                                                    classical_register,
                                                    tomo_set)
    return [Quantum_program,tomo_set,tomo_circuits]

def extract_data(results, circuit_name, tomo_set):
    tomo_data = tomo.tomography_data(results,circuit_name,tomo_set)
    return tomo_data