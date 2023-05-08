# -*- coding: utf-8 -*-
#pip install pylatexenc

#pip install qiskit

from qiskit import QuantumCircuit, ClassicalRegister, QuantumRegister, execute, assemble, Aer
from qiskit.tools.visualization import plot_histogram
from math import pi
import matplotlib.pyplot as plt

qreg_q = QuantumRegister(2, 'q')
creg_c = ClassicalRegister(2, 'c')
circuit = QuantumCircuit(qreg_q, creg_c)

circuit.draw(output='mpl')

circuit.h(qreg_q[0])
circuit.cx(qreg_q[0], qreg_q[1])
circuit.h(qreg_q[1])
circuit.measure(qreg_q[1], creg_c[1])
circuit.measure(qreg_q[0], creg_c[0])

circuit.draw(output='mpl')

sim = Aer.get_backend('qasm_simulator')

result = execute(circuit , backend = sim).result()

plot_histogram(result.get_counts(circuit))

from qiskit import IBMQ

IBMQ.save_account('9343920afba30a6123f31866d3c587e49d594c00dbe239c63e82c73b858672cdf71facd060cf6105e42013739fc1d939c42629a72e6e85e0c08c1742e2f1836a')

IBMQ.load_account()

provider = IBMQ.get_provider('ibm-q')

provider = IBMQ.get_provider(hub='ibm-q', group='open', project='main')
provider.backends()

qcomp = provider.get_backend('ibmq_qasm_simulator')

job = execute(circuit , backend = qcomp)

from qiskit.tools.monitor import job_monitor

job_monitor(job)

result = job.result()

plot_histogram(result.get_counts(circuit))