from fifo import Fifo

class PatientsLine:
    def __init__(self, patience_rate = 0):
        self.corona_plus_patients = Fifo(patience_rate ,"plus patients")
        self.corona_minus_patients = Fifo(patience_rate ,"minus patients")
        
    def elapse_time(self):
        self.corona_minus_patients.elapse_time()
        self.corona_plus_patients.elapse_time()
    
    def add_to_line(self, patient):
        if patient.corona_test_result == "+":
            self.corona_plus_patients.add_to_line(patient)
        else:
            self.corona_minus_patients.add_to_line(patient)
            
    def get_next_patient(self):
        next_patient = self.corona_plus_patients.get_next_patient()
        if next_patient == None:
            next_patient = self.corona_minus_patients.get_next_patient()
        return next_patient
    
    def get_plus_patients_length(self):
        return len(self.corona_plus_patients.line)

    def get_minus_patients_length(self):
        return len(self.corona_minus_patients.line)
    
    def get_line_length(self):
        return self.get_plus_patients_length() + self.get_minus_patients_length()