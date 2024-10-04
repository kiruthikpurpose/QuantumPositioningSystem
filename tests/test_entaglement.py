import unittest
from qps.entanglement import QuantumEntanglement

class TestEntanglement(unittest.TestCase):
    def setUp(self):
        self.qe = QuantumEntanglement()

    def test_entangle_particles(self):
        entangled_state = self.qe.entangle_particles()
        self.assertTrue(len(entangled_state) > 0)

    def test_measure_entanglement(self):
        measurement = self.qe.measure_entanglement()
        self.assertIsInstance(measurement, dict)

if __name__ == '__main__':
    unittest.main()
