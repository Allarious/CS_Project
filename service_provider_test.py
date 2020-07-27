import unittest
from service_provider import ServiceProvider
from patient import Patient

class TestServiceProvider(unittest.TestCase):
    
    def test_empty_service_provider(self):
        print("========= empty test =========")
        sp = ServiceProvider([3, 4])
        
        self.assertTrue(sp.does_accept_patient())
        
        sp.elapse_time()
        sp.elapse_time()
        
    def test_adding_to_perovider(self):
        print("========= add test =========")
        sp = ServiceProvider([2, 1, 4])
        
        sp.add_to_line(Patient("+", 2))
        sp.add_to_line(Patient("+", 5))
        sp.add_to_line(Patient("+", 4))
        sp.add_to_line(Patient("+", 1))
        sp.add_to_line(Patient("+", 3))
        sp.add_to_line(Patient("+", 7))
        sp.add_to_line(Patient("+", 3))

        self.assertEqual(7, sp.patients_line.get_line_length())
        
        sp.elapse_time()

        sp.add_to_line(Patient("+", 5))
        sp.add_to_line(Patient("+", 2))
        
        self.assertEqual(5, sp.patients_line.get_line_length())
        
        sp.elapse_time()

        self.assertEqual(4, sp.patients_line.get_line_length())

        sp.elapse_time()
        
        self.assertEqual(1, sp.patients_line.get_line_length())
        
        sp.elapse_time()
        sp.elapse_time()
        sp.elapse_time()
        sp.elapse_time()
        sp.elapse_time()
        
        
    
if __name__ == "__main__":
    unittest.main()