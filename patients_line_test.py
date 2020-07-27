import unittest
from patients_line import PatientsLine
from patient import Patient

class TestPatientsLine(unittest.TestCase):
    def test_empty_line(self):
        line = PatientsLine()
        
        self.assertEqual(0, line.get_plus_patients_length())
        self.assertEqual(0, line.get_minus_patients_length())
        self.assertEqual(0, line.get_line_length())
        self.assertIsNone(line.get_next_patient())
        
    def test_add_patients(self):
        line = PatientsLine()
        
        line.add_to_line(Patient("+", 2))
        line.add_to_line(Patient("+", 4))
        
        self.assertEqual(2, line.get_plus_patients_length())
        self.assertEqual(0, line.get_minus_patients_length())
        
        line.add_to_line(Patient("-", 3))

        self.assertEqual(2, line.get_plus_patients_length())
        self.assertEqual(1, line.get_minus_patients_length())
        
        line.elapse_time()
        
        self.assertEqual(2, line.get_plus_patients_length())
        self.assertEqual(1, line.get_minus_patients_length())
        
        line.elapse_time()
        
        self.assertEqual(1, line.get_plus_patients_length())
        self.assertEqual(1, line.get_minus_patients_length())
        
        line.elapse_time()
        
        self.assertEqual(1, line.get_plus_patients_length())
        self.assertEqual(0, line.get_minus_patients_length())
        
        line.elapse_time()
        
        self.assertEqual(0, line.get_plus_patients_length())
        self.assertEqual(0, line.get_minus_patients_length())
        
        line.elapse_time()
        line.elapse_time()
        line.elapse_time()
        line.elapse_time()
        line.elapse_time()
        line.elapse_time()
    
    def test_get_patients(self):
        line = PatientsLine()
        
        line.add_to_line(Patient("+", 2))
        line.add_to_line(Patient("-", 4))
        line.add_to_line(Patient("+", 3))
        line.add_to_line(Patient("-", 2))
        
        self.assertEqual("+", line.get_next_patient().corona_test_result)
        self.assertEqual("+", line.get_next_patient().corona_test_result)
        self.assertEqual("-", line.get_next_patient().corona_test_result)
        self.assertEqual("-", line.get_next_patient().corona_test_result)
        
        self.assertEqual(0, line.get_line_length())
        
        line.add_to_line(Patient("+", 2))
        line.add_to_line(Patient("-", 4))
        line.add_to_line(Patient("+", 3))
        line.add_to_line(Patient("-", 2))
        
        line.elapse_time()
        line.elapse_time()
        
        self.assertEqual("+", line.get_next_patient().corona_test_result)
        self.assertEqual("-", line.get_next_patient().corona_test_result)
        
        
    
if __name__ == "__main__":
    unittest.main()