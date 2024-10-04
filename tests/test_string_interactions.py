import unittest
from qps.string_interactions import StringInteractions

class TestStringInteractions(unittest.TestCase):
    def setUp(self):
        self.si = StringInteractions()

    def test_entangle_strings(self):
        circuit = self.si.entangle_strings()
        self.assertIsNotNone(circuit)

    def test_simulate_interaction(self):
        result = self.si.simulate_interaction()
        self.assertIsInstance(result, list)

    def test_measure_strings(self):
        result = self.si.measure_strings()
        self.assertIsInstance(result, dict)

if __name__ == '__main__':
    unittest.main()
