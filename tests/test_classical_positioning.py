import unittest
from qps.classical_positioning import ClassicalPositioning

class TestClassicalPositioning(unittest.TestCase):
    def setUp(self):
        self.cp = ClassicalPositioning(signal_speed=300000, distance=1500)

    def test_time_delay(self):
        delay = self.cp.calculate_time_delay()
        self.assertGreater(delay, 0)

    def test_estimate_position(self):
        position = self.cp.estimate_position(0.005)
        self.assertGreater(position, 0)

if __name__ == '__main__':
    unittest.main()
