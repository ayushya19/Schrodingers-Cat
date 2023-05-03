from flask import Flask, request, jsonify
from qiskit import QuantumCircuit, Aer, execute

#app = Flask(__name__)

#@app.route('/qiskit/probabilities', methods=['POST'])
def qiskit_probabilities():
    # get the states to measure from the JSON payload
    states = request.json['states']

    # create a quantum circuit with 2 qubits
    circuit = QuantumCircuit(2, 2)

    # apply the necessary gates to generate the states to measure
    if "01" in states:
        circuit.x(1)
    if "10" in states:
        circuit.x(0)
    if "11" in states:
        circuit.x(0)
        circuit.x(1)

    # measure the qubits and get the counts
    circuit.measure([1, 1], [0, 0])
    backend = Aer.get_backend('qasm_simulator')
    counts = execute(circuit, backend=backend, shots=1024).result().get_counts()

    # format the probabilities as a JSON response
    probabilities = {}
    for state in states:
        if state in counts:
            probabilities[state] = counts[state] / 1024
        else:
            probabilities[state] = 0

    return jsonify(probabilities)

#qiskit_probabilities()


#if __name__ == '__main__':
#    app.run(debug=True)
