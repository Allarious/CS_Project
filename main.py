from  service_provider import ServiceProvider
from patient import Patient
from doctors_rooms import DoctorsRooms

def elapse_time(reception, doctors):
    patients = reception.elapse_time()
    doctors.elapse_time()
    
    return patients

def add_inputs(reception, patient_entry_rate, patient_patience_rate):
    reception.add_to_line(Patient("+", patient_patiance_rate))
    reception.add_to_line(Patient("-", patient_patiance_rate))
    reception.add_to_line(Patient("-", patient_patiance_rate))
    

if __name__ == "__main__":
    
    # ====== Begin Initialization From File =====
    
    file = open("input.txt", "r")
    split_character = ","
    
    number_of_rooms, patient_entry_rate, patient_patiance_rate, reception_service_rate = list(map(int, file.readline().split(split_character)))
    print(number_of_rooms, patient_entry_rate, patient_patiance_rate, reception_service_rate)
    
    reception = ServiceProvider([reception_service_rate])
    doctors_rooms = DoctorsRooms()
    
    for line in range(number_of_rooms):
        doctors_service_rate = list(map(int, file.readline().split(split_character)))
        doctors_rooms.add_room(doctors_service_rate)
        
    # doctors_rooms.print_info()
    
    file.close()
    
    # ====== End Initialization ======
    
    for i in range(10000):
        
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
    