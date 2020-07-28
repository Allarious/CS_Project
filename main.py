from  service_provider import ServiceProvider
from patient import Patient
from doctors_rooms import DoctorsRooms
from time import time
import numpy as np
import matplotlib.pyplot as plt

def elapse_time(reception, doctors):
    patients = reception.elapse_time()
    doctors.elapse_time()
    
    return patients

def add_inputs(reception, patient_entry_rate, patient_patience_rate):
    
    number_of_patients = np.random.poisson(lam=patient_entry_rate)
    corona_tests = np.random.uniform(0, 1, number_of_patients)
    
    plus = 0
    minus = 0
    
    for p in range(number_of_patients):
        corona_test = "-" if corona_tests[p] > 0.1 else "+"
        
        if corona_test == "-":
            minus += 1
        elif corona_test == "+":
            plus += 1
        else:
            raise("Invalid test result")
        
        reception.add_to_line(Patient(corona_test, patient_patiance_rate))
            
    return number_of_patients, plus, minus
    

if __name__ == "__main__":
    
    # ====== Begin Initialization From File =====
    
    file = open("input.txt", "r")
    split_character = ","
    
    number_of_rooms, patient_entry_rate, patient_patiance_rate, reception_service_rate = list(map(int, file.readline().split(split_character)))
    # print(number_of_rooms, patient_entry_rate, patient_patiance_rate, reception_service_rate)
    
    reception = ServiceProvider([reception_service_rate], patient_patiance_rate, "reception")
    doctors_rooms = DoctorsRooms(patient_patiance_rate)
    
    for line in range(number_of_rooms):
        doctors_service_rate = list(map(int, file.readline().split(split_character)))
        doctors_rooms.add_room(doctors_service_rate)
        
    # doctors_rooms.print_info()
    
    file.close()
    
    # ====== End Initialization ======
    
    time_start = time()
    
    patient_goal = 10000
    flag1 = flag2 = flag3 = flag4 = flag5 = flag5 = flag6 = flag7 = flag8 = flag9 = True 
    total_number_of_patients = 0
    total_plus = 0
    total_minus = 0
    
    while True:
    
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
            print("No more patients are accepted, patients are waiting for service...")
            flag9 = False
        
        if total_number_of_patients < patient_goal:
            number_of_patients, plus, minus = add_inputs(reception, patient_entry_rate, patient_patiance_rate)
            total_number_of_patients += number_of_patients
            total_plus += plus
            total_minus += minus
            
        if total_number_of_patients >= patient_goal and reception.patients_line.get_line_length() == 0:
            break
        
        patients = elapse_time(reception, doctors_rooms)
        
        if len(patients) == 0:
            continue
        
        for patient in patients:
            next_room = doctors_rooms.get_next_room()
            doctors_rooms.add_to_room(next_room, patient)
    
    array_plus, array_minus, array_line_plus, array_line_minus, left_plus, left_minus = doctors_rooms.get_patients_data()
    
    array_plus.append(reception.current_plus_patients)
    array_minus.append(reception.current_minus_patients)
    array_line_plus.append(reception.get_fifo_plus_data())
    array_line_minus.append(reception.get_fifo_minus_data())
    left_plus += reception.get_left_plus_patients()
    left_minus += reception.get_left_minus_patients()
    
    np_plus = np.array(array_plus)
    np_minus = np.array(array_minus)
    np_line_plus = np.array(array_line_plus)
    np_line_minus = np.array(array_line_minus)
    
    time_end = doctors_rooms.get_time()
    
    print("Total number of patients : " + str(total_number_of_patients))
    print("Total number of plus patients : " + str(total_plus))
    print("Total number of minus patients : " + str(total_minus))
    
    #===== task for mean time in system
    print("Mean amount of time spent in system : " + str(round((np.sum(np_plus) + np.sum(np_minus))/total_number_of_patients, 2)))
    print("Mean amount of time spent in system (patients tested plus for corona) : " + str(round(np.sum(np_plus)/total_plus, 2)))
    print("Mean amount of time spent in system (patients not yet tested for corona) : " + str(round(np.sum(np_minus)/total_minus, 2)))
            
    #===== task for mean time in line
    print("Mean amount of time spent in line : " + str(round((np.sum(np_line_plus) + np.sum(np_line_minus))/total_number_of_patients, 2)))
    print("Mean amount of time spent in line (patients tested plus for corona) : " + str(round(np.sum(np_line_plus)/total_plus, 2)))
    print("Mean amount of time spent in line (patients not yet tested for corona) : " + str(round(np.sum(np_line_minus)/total_minus, 2)))
    
    #===== task for patients who left
    print("A total amount of " + str(left_plus + left_minus) + " left the hospital. this was a simulation of " + str(time_end) + " minutes. " + str(left_plus) + " of them were tested plus for corona and " + str(left_minus) + " of them were not tested yet.")
    
    #===== task for mean line length of reception and doctors rooms
    print("reception mean line length was : " + str(round((np.sum(np_line_plus[-1]) + np.sum(np_line_minus[-1])) / time_end, 2)) + " for " + str(time_end) + " minutes.")
    print("and doctors rooms line mean length was according to the following: ")
    for doctor_room_index in range(len(np_line_plus) - 1):
        print(str(round((np.sum(np_line_plus[doctor_room_index]) + np.sum(np_line_minus[doctor_room_index])) / time_end, 2)))
        
    #===== drawing the graphs 
    np_getting_service_cumulutive_plus = np_plus.sum(axis=0)
    np_getting_service_cumulutive_minus = np_minus.sum(axis=0)
    
    np_waiting_in_line_cumulutive_plus = np_line_plus.sum(axis=0)
    np_waiting_in_line_cumulutive_minus = np_line_minus.sum(axis=0)
    
    plt.figure(0)
    plt.title("answering frequency - blue (plus), orange (not tested), green (overall)")
    plt.plot(range(time_end), np_getting_service_cumulutive_plus)
    plt.plot(range(time_end), np_getting_service_cumulutive_minus)
    plt.plot(range(time_end), np.add(np_getting_service_cumulutive_plus, np_getting_service_cumulutive_minus))
    
    plt.figure(1)
    plt.title("waiting time frequency - blue (plus), orange (not tested), green (overall)")
    plt.plot(range(time_end), np_waiting_in_line_cumulutive_plus)
    plt.plot(range(time_end), np_waiting_in_line_cumulutive_minus)
    plt.plot(range(time_end), np.add(np_waiting_in_line_cumulutive_plus, np_waiting_in_line_cumulutive_minus))
    
    plt.figure(2)
    plt.title("patients in the simulation - blue (plus), orange (not tested), green (overall)")
    plt.plot(range(time_end), np.add(np_waiting_in_line_cumulutive_plus, np_getting_service_cumulutive_plus))
    plt.plot(range(time_end), np.add(np_waiting_in_line_cumulutive_minus, np_getting_service_cumulutive_minus))
    plt.plot(range(time_end), np.add(np_waiting_in_line_cumulutive_minus, np.add(np_waiting_in_line_cumulutive_plus, np.add(np_getting_service_cumulutive_minus, np_getting_service_cumulutive_plus))))
    
    plt.figure(3)
    plt.title("frequency of patients")
    name_labels = ["plus", "not tested"]
    patients_numbers = [total_plus, total_minus]
    plt.bar(name_labels, patients_numbers)
    
    plt.show()
    
    
    
    
        
    print("Simulation completed in : " + str(round(time() - time_start, 2)) + "s")
    