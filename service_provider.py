from patients_line import PatientsLine
from numpy import random
from math import ceil

class ServiceProvider:
    def __init__(self, array_of_means, patience_rate = 0, work = "doctor"):
        self.answering_time_plus = []
        self.answering_time_minus = []
        self.work = work
        self.current_minus_patients = []
        self.current_plus_patients = []
        self.patients_line = PatientsLine(patience_rate)
        self.number_of_service_providers = len(array_of_means)
        self.current_tables = [0] * self.number_of_service_providers
        self.current_patients = [0] * self.number_of_service_providers
        self.array_of_means = array_of_means
        
    def __get_service_time(self, index, patient):
        if index >= self.number_of_service_providers:
            raise("index more than number of providers.")
            return None
        if self.work == "doctor":
            service_time = random.exponential(self.array_of_means[index])
        else:
            # it might be zero !!
            service_time = random.poisson(self.array_of_means[index])
            # i dont know about this one!
            if service_time == 0:
                service_time = 1
        self.current_tables[index] = service_time
        self.current_patients[index] = patient
        if patient.corona_test_result == "+":
            self.answering_time_plus.append(ceil(service_time))
        else:
            self.answering_time_minus.append(ceil(service_time))
        return service_time
    
    def get_fifo_plus_data(self):
        return self.patients_line.corona_plus_patients.current_patients_waiting
    
    def get_fifo_minus_data(self):
        return self.patients_line.corona_minus_patients.current_patients_waiting
    
    def get_left_plus_patients(self):
        return self.patients_line.corona_plus_patients.patients_left_the_hospital
    
    def get_left_minus_patients(self):
        return self.patients_line.corona_minus_patients.patients_left_the_hospital 
    
    def get_time(self):
        return self.patients_line.corona_plus_patients.time
    
    def does_accept_patient(self):
        if 0 in self.current_tables:
            return True
        return False
    
    def get_number_of_plus_patients(self):
        number_of_plus_patients = 0
        for patient in self.current_patients:
            if patient == 0 :
                continue
            if patient.corona_test_result == "+":
                number_of_plus_patients += 1
                
        return number_of_plus_patients
    
    def give_service_to_patient(self):
        service_time = 0
        table_number = 0
        if self.does_accept_patient == False:
            raise("there are no empty tables.")
            return
        
        for table_index in range(len(self.current_tables)):
            if self.current_tables[table_index] == 0 and self.patients_line.get_line_length() != 0:
                patient = self.patients_line.get_next_patient()
                service_time = self.__get_service_time(table_index, patient)
                # print('giving service to patient')
                table_number = table_index + 1
                break
        
        if service_time == 0:
            raise("something went wrong, serice time can not be zero.")
            return

        if table_number == 0:
            raise("something went wrong, table number can not be zero.")
            return
        
        return service_time, table_number
    
    def get_number_of_current_patients(self):
        number_of_busy_tables = 0
        for table in self.current_tables:
            if table != 0:
                number_of_busy_tables += 1
                
        return number_of_busy_tables
                
    
    def add_to_line(self, patient):
        self.patients_line.add_to_line(patient)
        
    def elapse_time(self):
        while(True):

            if self.patients_line.get_line_length() == 0:
                # print("no patients in line to be served.")
                break

            if 0 in self.current_tables:
                self.give_service_to_patient()
            else:
                break
            
        plus_patients = self.get_number_of_plus_patients()
        self.current_minus_patients.append(self.get_number_of_current_patients() - plus_patients)
        self.current_plus_patients.append(plus_patients)
        
        self.patients_line.elapse_time()
        
        out_patients = []
        
        # print(self.current_tables)
        
        for table in range(len(self.current_tables)):
            if 0 < self.current_tables[table] <= 1:
                out_patients.append(self.current_patients[table])
            self.current_tables[table] = max(0, self.current_tables[table] - 1)
            
        # for patients in out_patients:
        #     print(patients.get_info_about_patient())
        return out_patients
    
    def print_state(self):
        print("line length is " + str(self.patients_line.get_line_length) + ".")
        print("there are " + str(self.number_of_service_providers) + " providers.")
        print("current tables:")
        print(self.current_tables)
        print("mean arrays are:")
        print(self.array_of_means)