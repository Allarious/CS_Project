from patient import Patient

class Fifo:
    def __init__(self, patience_rate = 0,  name = 'fifo line'):
        self.patience_rate = patience_rate
        self.waited = []
        self.line = []
        self.name = name
        self.time = 0
        self.current_patients_waiting = []
        self.patients_left_the_hospital = 0
        # print("Fifo named " + name + " Created")
    
    def add_to_line(self, patient):
        patient.set_entry_time(self.time)
        self.line.append(patient)
    
    def elapse_time(self):
        self.current_patients_waiting.append(len(self.line))
        # print("elapsing time in " + self.name + " going from " + str(self.time) + " to " + str(self.time + 1) + ".")
        self.time = self.time + 1
        self.__check_if_patients_leave()
        return self.time
    
    def __check_if_patients_leave(self):
        next_line = []
        for patient in self.line:
            if patient.entry_time + patient.patience_in_minutes <= self.time:
                # print("a patient left " + self.name)
                self.patients_left_the_hospital += 1
                continue
            next_line.append(patient)
        self.line = next_line
        
    def get_next_patient(self):
        if len(self.line) == 0:
            return None
        else:
            self.line[0].patience_in_minutes -= self.time - self.line[0].entry_time
            self.waited.append(self.patience_rate - self.line[0].patience_in_minutes)
            return self.line.pop(0)
        
    def print_patients(self):
        for patient in self.line:
            print(patient.get_info_about_patient())