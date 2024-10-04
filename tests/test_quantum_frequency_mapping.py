import unittest
from qps.quantum_frequency_mapping import QuantumFrequencyMapping

class TestQuantumFrequencyMapping(unittest.TestCase):
    def setUp(self):
        self.qfm = QuantumFrequencyMapping(frequency=5)

    def test_string_vibrations(self):
        vibrations = self.qfm.calculate_string_vibrations()
        self.assertIsNotNone(vibrations)

    def test_map_to_position(self):
        position = self.qfm.map_to_position(entangled_state=[1, 0])
        self.assertIsInstance(position, (int, float))

if __name__ == '__main__':
    unittest.main()
