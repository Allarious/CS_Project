from service_provider import ServiceProvider

class DoctorsRooms:
    def __init__(self):
        self.doctors_rooms = []
        
    def add_room(self, doctors_service_rate):
        self.doctors_rooms.append(ServiceProvider(doctors_service_rate))
        
    def elapse_time(self):
        for room in self.doctors_rooms:
            room.elapse_time()
            
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