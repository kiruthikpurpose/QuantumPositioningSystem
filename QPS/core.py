from qiskit import QuantumCircuit, Aer, execute
from .entanglement import create_entangled_pair, measure_entanglement

class QuantumPositioningSystem:
    def __init__(self):
        self.entangled_pair = create_entangled_pair()

    def position(self, particle_id):
        if particle_id == 0:
            result = measure_entanglement(self.entangled_pair, 0)
        elif particle_id == 1:
            result = measure_entanglement(self.entangled_pair, 1)
        else:
            raise ValueError("Invalid particle_id. Must be 0 or 1.")
        return result

    def simulate(self):
        backend = Aer.get_backend('statevector_simulator')
        job = execute(self.entangled_pair, backend)
        result = job.result().get_statevector()
        return result
