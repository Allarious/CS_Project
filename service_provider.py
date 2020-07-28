from patients_line import PatientsLine

class ServiceProvider:
    def __init__(self, array_of_means):
        self.patients_line = PatientsLine()
        self.number_of_service_providers = len(array_of_means)
        self.current_tables = [0] * self.number_of_service_providers
        self.current_patients = [0] * self.number_of_service_providers
        self.array_of_means = array_of_means
        
    def __get_service_time(self, index, patient):
        if index >= self.number_of_service_providers:
            raise("index more than number of providers.")
            return None
        service_time = self.array_of_means[index]
        self.current_tables[index] = service_time
        self.current_patients[index] = patient
        return service_time
    
    def does_accept_patient(self):
        if 0 in self.current_tables:
            return True
        return False
    
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
                print('giving service to patient')
                table_number = table_index + 1
                break
        
        if service_time == 0:
            raise("something went wrong, serice time can not be zero.")
            return

        if table_number == 0:
            raise("something went wrong, table number can not be zero.")
            return
        
        return service_time, table_number
    
    def add_to_line(self, patient):
        self.patients_line.add_to_line(patient)
        
    def elapse_time(self):
        while(True):

            if self.patients_line.get_line_length() == 0:
                print("no patients in line to be served.")
                break

            if 0 in self.current_tables:
                self.give_service_to_patient()
            else:
                break
            
            
        self.patients_line.elapse_time()
        
        out_patients = []
        
        print(self.current_tables)
        
        for table in range(len(self.current_tables)):
            if self.current_tables[table] == 1:
                out_patients.append(self.current_patients[table])
            self.current_tables[table] = max(0, self.current_tables[table] - 1)
            
        for patients in out_patients:
            print(patients.get_info_about_patient())
        return out_patients
            
    def print_state(self):
        print("line length is " + str(self.patients_line.get_line_length) + ".")
        print("there are " + str(self.number_of_service_providers) + " providers.")
        print("current tables:")
        print(self.current_tables)
        print("mean arrays are:")
        print(self.array_of_means)