import unittest
from src.calculations import calculate_weight_on_planets, convert_weight_to_unit

class TestCalculateWeightOnPlanets(unittest.TestCase):
    def test_positive_earth_weight(self):
        earth_weight = 70
        expected = {
            "Mercúrio": 26.6,
            "Vênus": 63.7,
            "Marte": 26.6,
            "Júpiter": 163.8,
            "Saturno": 74.2,
            "Urano": 64.4,
            "Netuno": 83.3,
            "Plutão": 4.2,
            "Sol": 1890.7
        }
        result = calculate_weight_on_planets(earth_weight)
        for planet, weight in expected.items():
            self.assertAlmostEqual(result[planet], weight, places=1)

    def test_zero_weight(self):
        self.assertEqual(calculate_weight_on_planets(0), {
            "Mercúrio": 0.0,
            "Vênus": 0.0,
            "Marte": 0.0,
            "Júpiter": 0.0,
            "Saturno": 0.0,
            "Urano": 0.0,
            "Netuno": 0.0,
            "Plutão": 0.0,
            "Sol": 0.0
        })

    def test_negative_weight(self):
        earth_weight = -70
        result = calculate_weight_on_planets(earth_weight)
        for planet, weight in result.items():
            self.assertTrue(weight < 0)

    def test_convert_weight_to_unit(self):
        weight_kg = 10
        self.assertAlmostEqual(convert_weight_to_unit(weight_kg, "lb"), 22.0462, places=4)
        self.assertAlmostEqual(convert_weight_to_unit(weight_kg, "oz"), 352.74, places=2)
        self.assertAlmostEqual(convert_weight_to_unit(weight_kg, "kg"), 10, places=4)

if __name__ == "__main__":
    unittest.main()
