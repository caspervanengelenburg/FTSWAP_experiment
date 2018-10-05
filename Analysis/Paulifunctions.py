# -*- coding: utf-8 -*-
"""
Created on Wed Sep 26 16:59:16 2018

@author: Jarnd
"""


def calc_trace_P1prod(indices):
    '''
    Calculates the trace of 4 normalized paulis (including identity) with indices in a list.
    ind: I = 0, X = 1, Y = 2, Z = 3.
    '''
    ind = indices.copy()
    Idencount = ind.count(0)  # calculate number of I's
    while Idencount > 0:  # Get rid of I's to use the pauli trace relations
        ind.remove(0)
        Idencount = ind.count(0)
    if len(ind) == 4:  # Means 4 non-I paulis left
        abcd = kron(ind[0], ind[1])*kron(ind[2], ind[3])
        acbd = kron(ind[0], ind[2])*kron(ind[1], ind[3])
        adbc = kron(ind[0], ind[3])*kron(ind[1], ind[2])
        trace = 2*int(abcd - acbd + adbc)  # Trace relation for 4 paulis
    elif len(ind) == 3:  # Means 3 non-I paulis left
        # Trace relation for 3 paulis
        trace = 2*1j*int(levi(ind[0], ind[1], ind[2]))
    elif len(ind) == 2:  # Means 2 non-I paulis left
        trace = 2*int(kron(ind[0], ind[1]))  # Trace relation for 2 paulis
    elif len(ind) == 1:  # Means 1 non-I paulis left
        trace = 0  # All non-I are traceless
    elif len(ind) == 0:  # Means 0 non-I paulis left
        trace = 2  # Trace of identity
    return trace*(1/4)  # divide by 4 because the paulis are normalized


def calc_trace_P2prod(paulilist):
    '''
    Calculates the trace of up to 4 normalized P2 elements (including identity).
    P2 elements should be represented as tuples of two indices of the P1 elements it is a tensor product of.
    ind. I = 0, X = 1, Y = 2, Z = 3.
    '''
    indices0 = []
    indices1 = []
    for pauli in paulilist:
        indices0.append(pauli[0])
        indices1.append(pauli[1])
    trace0 = calc_trace_P1prod(indices0)
    trace1 = calc_trace_P1prod(indices1)
    return trace0*trace1


def kron(a, b):
    if a == b:
        return 1
    else:
        return 0


def levi(a, b, c):
    if a+b+c == 6:
        return ((b-a) % 3)*(-2) + 3
    else:
        return 0
