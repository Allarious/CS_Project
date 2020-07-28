from service_provider import ServiceProvider

class DoctorsRooms:
    def __init__(self):
        self.doctors_rooms = []
        
    def add_room(self, doctors_service_rate):
        self.doctors_rooms.append(ServiceProvider(doctors_service_rate))
    
    def get_time(self):
        if len(self.doctors_rooms) == 0:
            raise("there should be at least one doctors room.")
        return self.doctors_rooms[0].get_time()
    
    def elapse_time(self):
        for room in self.doctors_rooms:
            room.elapse_time()
            
    def get_patients_data(self):
        array_plus = []
        array_minus = []
        array_line_plus = []
        array_line_minus = []
        left_plus = 0
        left_minus = 0
        for doctors_room in self.doctors_rooms:
            array_plus.append(doctors_room.current_plus_patients)
            array_minus.append(doctors_room.current_minus_patients)
            array_line_plus.append(doctors_room.get_fifo_plus_data())
            array_line_minus.append(doctors_room.get_fifo_minus_data())
            left_plus = doctors_room.get_left_plus_patients()
            left_minus = doctors_room.get_left_minus_patients()
            
        return array_plus, array_minus, array_line_plus, array_line_minus, left_plus, left_minus
            
    def get_next_room(self):
        if len(self.doctors_rooms) == 0:
            raise("there should be at least one doctor room.")
        
        mini = 0
        
        for room_index in range(len(self.doctors_rooms)):
            if self.doctors_rooms[room_index].does_accept_patient():
                return room_index
            line_length = self.doctors_rooms[room_index].patients_line.get_line_length()
            if line_length < self.doctors_rooms[mini].patients_line.get_line_length():
                mini = room_index
        
        return mini
    
    def add_to_room(self, room_index, patient):
        self.doctors_rooms[room_index].add_to_line(patient)
        
    def print_info(self):
        print("number of rooms are : " + str(len(self.doctors_rooms)))
        for room_index in range(len(self.doctors_rooms)):
            print("info about room #" + str(room_index) + " : ")
            print("service rate is : " + str(self.doctors_rooms[room_index].array_of_means))
            print("length of this rooms line is : " + str(self.doctors_rooms[room_index].patients_line.get_line_length()))