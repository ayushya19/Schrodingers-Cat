from flask import Flask, request, jsonify
from qiskit import QuantumCircuit, Aer, execute

app = Flask(__name__)

@app.route('/qiskit/probabilities', methods=['POST'])
def get_probabilities():
    states = request.json['states']

    # create a quantum circuit with 2 qubits
    circuit = QuantumCircuit(2, 2)

    # apply the necessary gates to generate the states to measure
    circuit.h(0)
    circuit.h(1)
    circuit.measure(0,0)
    circuit.measure(1,1)
    backend = Aer.get_backend('qasm_simulator')
    counts = execute(circuit, backend=backend, shots=1024).result().get_counts()
    return jsonify(counts)

if __name__ == '__main__':
    app.run(debug=True)
