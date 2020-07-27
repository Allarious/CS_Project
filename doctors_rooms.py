from service_provider import ServiceProvider

class DoctorsRooms:
    def __init__(self):
        self.doctors_rooms = []
        
    def add_room(self, doctors_service_rate):
        self.doctors_rooms.append(ServiceProvider(doctors_service_rate))
        
    def print_info(self):
        print("number of rooms are : " + str(len(self.doctors_rooms)))
        for room_index in range(len(self.doctors_rooms)):
            print("info about room #" + str(room_index) + " : ")
            print("service rate is : " + str(self.doctors_rooms[room_index].array_of_means))
            print("length of this rooms line is : " + str(self.doctors_rooms[room_index].patients_line.get_line_length()))