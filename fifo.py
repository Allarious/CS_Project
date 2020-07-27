from patient import Patient

class Fifo:
    def __init__(self, name = 'fifo line'):
        self.line = []
        self.name = name
        self.time = 0
        print("Fifo named " + name + " Created")
    
    def add_to_line(self, patient):
        patient.set_entry_time(self.time)
        self.line.append(patient)
    
    def elapse_time(self):
        print("elapsing time in " + self.name + " going from " + str(self.time) + " to " + str(self.time + 1) + ".")
        self.time = self.time + 1
        self.__check_if_patients_leave()
        return self.time
    
    def __check_if_patients_leave(self):
        next_line = []
        for patient in self.line:
            if patient.entry_time + patient.patience_in_minutes <= self.time:
                print("a patient left " + self.name)
                continue
            next_line.append(patient)
        self.line = next_line
        
    def get_next_patient(self):
        if len(self.line) == 0:
            return None
        else:
            return self.line.pop(0)
        
    def print_patients(self):
        for patient in self.line:
            print(patient.get_info_about_patient())