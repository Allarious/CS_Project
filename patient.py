class Patient:
    def __init__(self, corona_test_result, patience_in_minutes):
        self.corona_test_result = corona_test_result
        self.patience_in_minutes = patience_in_minutes
        print("Patient Created")
    
    def set_entry_time(self, time):
        self.entry_time = time

    def get_info_about_patient(self):
        return "corona test : " + str(self.corona_test_result) + ", entry time : " + str(self.entry_time) + ", patience : " + str(self.patience_in_minutes) + ", will leave in : " + str(self.entry_time + self.patience_in_minutes)
        