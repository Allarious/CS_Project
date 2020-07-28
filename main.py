from  service_provider import ServiceProvider
from patient import Patient
from doctors_rooms import DoctorsRooms
from time import time
from numpy import random

def elapse_time(reception, doctors):
    patients = reception.elapse_time()
    doctors.elapse_time()
    
    return patients

def add_inputs(reception, patient_entry_rate, patient_patience_rate):
    
    number_of_patients = random.poisson(lam=patient_entry_rate)
    corona_tests = random.uniform(0, 1, number_of_patients)
    
    for p in range(number_of_patients):
        reception.add_to_line(Patient("-" if corona_tests[p] > 0.1 else "+" , patient_patiance_rate))
    

if __name__ == "__main__":
    
    # ====== Begin Initialization From File =====
    
    file = open("input.txt", "r")
    split_character = ","
    
    number_of_rooms, patient_entry_rate, patient_patiance_rate, reception_service_rate = list(map(int, file.readline().split(split_character)))
    print(number_of_rooms, patient_entry_rate, patient_patiance_rate, reception_service_rate)
    
    reception = ServiceProvider([reception_service_rate], "reception")
    doctors_rooms = DoctorsRooms()
    
    for line in range(number_of_rooms):
        doctors_service_rate = list(map(int, file.readline().split(split_character)))
        doctors_rooms.add_room(doctors_service_rate)
        
    # doctors_rooms.print_info()
    
    file.close()
    
    # ====== End Initialization ======
    
    time_start = time()
    
    for i in range(100):
        
        print("*****")
        print("time: " + str(i))
        print("*****")
        
        add_inputs(reception, patient_entry_rate, patient_patiance_rate)
        
        patients = elapse_time(reception, doctors_rooms)
        
        if len(patients) == 0:
            continue
        
        for patient in patients:
            next_room = doctors_rooms.get_next_room()
            doctors_rooms.add_to_room(next_room, patient)
            
        print("==========")
        print(reception.patients_line.get_line_length())
        doctors_rooms.print_info()
        
    print("Simulation completed in : " + str(time() - time_start))
    