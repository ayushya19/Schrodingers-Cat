from qiskit import QuantumCircuit, ClassicalRegister, QuantumRegister, execute, assemble, Aer
from qiskit.tools.visualization import plot_histogram
from math import pi
import matplotlib.pyplot as plt
from flask import Flask
from qiskit.tools.monitor import job_monitor
from qiskit import IBMQ

#creating a flask 
app = Flask(__name__)

@app.route('/')
def index():
    qreg_q = QuantumRegister(2, 'q')
    creg_c = ClassicalRegister(2, 'c')
    circuit = QuantumCircuit(qreg_q, creg_c)

    circuit.draw(output='mpl')
    #define qubits
    circuit.h(qreg_q[0])
    circuit.cx(qreg_q[0], qreg_q[1])
    circuit.h(qreg_q[1])
    circuit.measure(qreg_q[1], creg_c[1])
    circuit.measure(qreg_q[0], creg_c[0])

    circuit.draw(output='mpl')
    
    #backend simulator
    sim = Aer.get_backend('qasm_simulator')

    #getting result
    result1 = execute(circuit , backend = sim).result()

    #connecting to ibm account
    IBMQ.save_account('9343920afba30a6123f31866d3c587e49d594c00dbe239c63e82c73b858672cdf71facd060cf6105e42013739fc1d939c42629a72e6e85e0c08c1742e2f1836a')

    IBMQ.load_account()

    provider = IBMQ.get_provider('ibm-q')

    provider = IBMQ.get_provider(hub='ibm-q', group='open', project='main')
    provider.backends()

    #ibm backend simulator 
    qcomp = provider.get_backend('ibmq_qasm_simulator')

    job = execute(circuit , backend = qcomp)

    job_monitor(job)

    #result for ibm 
    result = job.result()

    #convet result in dictionary form 
    counts = result.get_counts(circuit)
    counts1 = result1.get_counts(circuit)

    return [counts1 , counts]

if __name__ == "__main__":
  app.run(debug=True)