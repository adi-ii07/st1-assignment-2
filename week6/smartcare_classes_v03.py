class Patient:
    def __init__(self, patient_information):
        self.patient_information = patient_information

    def create_patient(self):
        pass

    def view_patient_information(self):
        pass


class Practitioner:
    def __init__(self, practitioner_information):
        self.practitioner_information = practitioner_information

    def store_practitioner_information(self):
        pass


class Appointment:
    def __init__(self, appointment_time, appointment_status,
                 appointment_information, patient, practitioner):
        self.appointment_time = appointment_time
        self.appointment_status = appointment_status
        self.appointment_information = appointment_information
        self.patient = patient
        self.practitioner = practitioner

    def create_appointment(self):
        pass

    def display_appointment(self):
        pass

    def retrieve_appointment(self):
        pass