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
        
    return number_of_patients
    

if __name__ == "__main__":
    
    # ====== Begin Initialization From File =====
    
    file = open("input.txt", "r")
    split_character = ","
    
    number_of_rooms, patient_entry_rate, patient_patiance_rate, reception_service_rate = list(map(int, file.readline().split(split_character)))
    # print(number_of_rooms, patient_entry_rate, patient_patiance_rate, reception_service_rate)
    
    reception = ServiceProvider([reception_service_rate], "reception")
    doctors_rooms = DoctorsRooms()
    
    for line in range(number_of_rooms):
        doctors_service_rate = list(map(int, file.readline().split(split_character)))
        doctors_rooms.add_room(doctors_service_rate)
        
    # doctors_rooms.print_info()
    
    file.close()
    
    # ====== End Initialization ======
    
    time_start = time()
    
    patient_goal = 100
    flag1 = flag2 = flag3 = flag4 = flag5 = flag5 = flag6 = flag7 = flag8 = flag9 = True 
    total_number_of_patients = 0
    
    while True:
        
        # print("*****")
        # print("time: " + str(i))
        # print("*****")
        
        
        if flag1 and total_number_of_patients >= patient_goal/10:
            print("10% in " + str(round(time() - time_start, 2)) + "s")
            flag1 = False

        if flag2 and total_number_of_patients >= patient_goal/10 * 2 :
            print("20% in " + str(round(time() - time_start, 2)) + "s")
            flag2 = False
            
        if flag3 and total_number_of_patients >= patient_goal/10 * 3 :
            print("30% in " + str(round(time() - time_start, 2)) + "s")
            flag3 = False
            
        if flag4 and total_number_of_patients >= patient_goal/10 * 4 :
            print("40% in " + str(round(time() - time_start, 2)) + "s")
            flag4 = False
            
        if flag5 and total_number_of_patients >= patient_goal/10 * 5 :
            print("50% in " + str(round(time() - time_start, 2)) + "s")
            flag5 = False
            
        if flag6 and total_number_of_patients >= patient_goal/10 * 6 :
            print("60% in " + str(round(time() - time_start, 2)) + "s")
            flag6 = False
            
        if flag7 and total_number_of_patients >= patient_goal/10 * 7 :
            print("70% in " + str(round(time() - time_start, 2)) + "s")
            flag7 = False
            
        if flag8 and total_number_of_patients >= patient_goal/10 * 8 :
            print("80% in " + str(round(time() - time_start, 2)) + "s")
            flag8 = False
            
        if flag9 and total_number_of_patients >= patient_goal/10 * 9 :
            print("90% in " + str(round(time() - time_start, 2)) + "s")
            flag9 = False
            
        if total_number_of_patients >= patient_goal:
            break
        
        
        number_of_patients = add_inputs(reception, patient_entry_rate, patient_patiance_rate)
        
        total_number_of_patients += number_of_patients
        
        patients = elapse_time(reception, doctors_rooms)
        
        if len(patients) == 0:
            continue
        
        for patient in patients:
            next_room = doctors_rooms.get_next_room()
            doctors_rooms.add_to_room(next_room, patient)
            
        # print("==========")
        # print(reception.patients_line.get_line_length())
        # doctors_rooms.print_info()
        
    print("Simulation completed in : " + str(round(time() - time_start, 2)) + "s")
    