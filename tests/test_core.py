import unittest
from qps.core import QuantumPositioningSystem

class TestCore(unittest.TestCase):
    def setUp(self):
        self.qps = QuantumPositioningSystem()

    def test_initialize(self):
        self.assertIsNotNone(self.qps)

    def test_positioning(self):
        position = self.qps.calculate_position()
        self.assertIsInstance(position, dict)

if __name__ == '__main__':
    unittest.main()
