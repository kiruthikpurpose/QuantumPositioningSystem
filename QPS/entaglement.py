from qiskit import QuantumCircuit

def create_entangled_pair():
    qc = QuantumCircuit(2)
    qc.h(0)
    qc.cx(0, 1)
    return qc

def measure_entanglement(qc, particle):
    qc.measure_all()
    return qc
