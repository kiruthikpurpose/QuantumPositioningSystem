import unittest
from qps.higher_dimensional_fields import HigherDimensionalFields

class TestHigherDimensionalFields(unittest.TestCase):
    def setUp(self):
        self.hdf = HigherDimensionalFields(dimensions=5)

    def test_generate_field(self):
        field = self.hdf.generate_field()
        self.assertEqual(field.shape, (5, 5))

    def test_apply_field_to_entanglement(self):
        modified_state = self.hdf.apply_field_to_entanglement([1, 0, 0, 0, 0])
        self.assertIsInstance(modified_state, list)

if __name__ == '__main__':
    unittest.main()
