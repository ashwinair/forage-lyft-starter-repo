import unittest
from tire.tire_types.carrigan_tires import CarriganTires
from tire.tire_types.octoprime_tires import OctoprimeTires

class TestCarriganTires(unittest.TestCase):
    def test_need_service_true(self):
        tire_wear = [0.1,0.2,0.5,0.9]
        tire = CarriganTires(tire_wear)
        self.assertTrue(tire.needs_service())

    def test_need_service_false(self):
        tire_wear = [0.1,0.8,0.1,0.7]
        tire = CarriganTires(tire_wear)
        self.assertFalse(tire.needs_service())
        
class TestOctoprimeTires(unittest.TestCase):
    def test_need_service_true(self):
        tire_wear = [0.9,0.7,0.8,0.9]
        tire = OctoprimeTires(tire_wear)
        self.assertTrue(tire.needs_service())

    def test_need_service_false(self):
        tire_wear = [0.1,0.2,0.5,0.9]
        tire = OctoprimeTires(tire_wear)
        self.assertFalse(tire.needs_service())