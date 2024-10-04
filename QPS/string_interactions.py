from qiskit import QuantumCircuit, Aer, execute

class StringInteractions:
    def __init__(self):
        self.qc = QuantumCircuit(2)

    def entangle_strings(self):
        # Simulate entangling two particles (strings)
        self.qc.h(0)
        self.qc.cx(0, 1)
        return self.qc

    def simulate_interaction(self):
        backend = Aer.get_backend('statevector_simulator')
        job = execute(self.qc, backend)
        return job.result().get_statevector()
    
    def measure_strings(self):
        self.qc.measure_all()
        backend = Aer.get_backend('qasm_simulator')
        job = execute(self.qc, backend)
        return job.result().get_counts()
