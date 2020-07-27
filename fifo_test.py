import unittest
from fifo import Fifo
from patient import Patient

class TestFifo(unittest.TestCase):
    def test_empty_fifo(self):
        fifo = Fifo()
        self.assertEqual(1, fifo.elapse_time())
        self.assertIsNone(fifo.get_next_patient())
        
    def test_add_patients(self):
        fifo = Fifo()
        
        fifo.add_to_line(Patient("+", 3))
        fifo.add_to_line(Patient("+", 6))
        fifo.add_to_line(Patient("+", 1))
        fifo.add_to_line(Patient("+", 2))
        fifo.add_to_line(Patient("+", 4))
        
        self.assertEqual(5, len(fifo.line))
        fifo.elapse_time()    
        self.assertEqual(4, len(fifo.line))
        fifo.elapse_time()    
        self.assertEqual(3, len(fifo.line))
        fifo.elapse_time()    
        self.assertEqual(2, len(fifo.line))
        fifo.elapse_time()    
        self.assertEqual(1, len(fifo.line))
        fifo.elapse_time()    
        self.assertEqual(1, len(fifo.line))
        fifo.elapse_time()    
        self.assertEqual(0, len(fifo.line))
    
    def test_patience_time(self):
        fifo = Fifo()
        
        fifo.add_to_line(Patient("+", 2))
        fifo.add_to_line(Patient("+", 3))
        fifo.add_to_line(Patient("+", 5))
        
        fifo.elapse_time()
        
        self.assertEqual(1, fifo.get_next_patient().patience_in_minutes)
        
        fifo.elapse_time()
        fifo.elapse_time()
        
        self.assertEqual(2, fifo.get_next_patient().patience_in_minutes)
        
        self.assertEqual(0, len(fifo.line))
        self.assertIsNone(fifo.get_next_patient())
    
if __name__ == "__main__":
    unittest.main()