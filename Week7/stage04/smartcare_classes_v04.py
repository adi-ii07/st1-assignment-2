
from enum import Enum

class AppointmentStatus(Enum):
    BOOKED = "Booked"
    CANCELLED = "Cancelled"

class Patient:
    def __init__(self, patient_information: str):
        if not isinstance(patient_information, str):
            raise TypeError("Patient information must be a string")

        if not patient_information.strip():
            raise ValueError("Patient information cannot be empty")

        self.patient_information = patient_information

    def create_patient(self):
        return self.patient_information

    def view_patient_information(self):
        return self.patient_information

class Practitioner:
    def __init__(self, identifier: str, name: str, specialty: str):
        for value in (identifier, name, specialty):
            if not isinstance(value, str):
                raise TypeError("Practitioner details must be strings")
            if not value.strip():
                raise ValueError("Practitioner details cannot be empty")

        self.identifier = identifier
        self.name = name
        self.specialty = specialty
        self.practitioner_information = name

    def store_practitioner_information(self):
        return self.practitioner_information


class Appointment:
    appointments = []

    def __init__(self, appointment_time: str,
                 appointment_status: AppointmentStatus,
                 appointment_information: str,
                 patient: Patient,
                 practitioner: Practitioner):

        if not isinstance(patient, Patient):
            raise TypeError("Patient must be a Patient object")

        if not isinstance(practitioner, Practitioner):
            raise TypeError("Practitioner must be a Practitioner object")

        if not isinstance(appointment_status, AppointmentStatus):
            raise TypeError("Appointment status must be an AppointmentStatus")

        if not isinstance(appointment_information, str):
            raise TypeError("Appointment information must be a string")

        if not appointment_information.strip():
            raise ValueError("Appointment information cannot be empty")

        if not isinstance(appointment_time, str):
            raise TypeError("Appointment time must be a string")

        if not appointment_time.strip():
            raise ValueError("Appointment time cannot be empty")

        self.appointment_time = appointment_time
        self.appointment_status = appointment_status
        self.appointment_information = appointment_information
        self.patient = patient
        self.practitioner = practitioner

    def create_appointment(self):
        for existing in Appointment.appointments:
            if (existing.practitioner is self.practitioner
                    and existing.appointment_time == self.appointment_time
                    and existing.appointment_status == AppointmentStatus.BOOKED):
                raise ValueError("Practitioner is already booked at this time")
        Appointment.appointments.append(self)

        return {
            "appointment_time": self.appointment_time,
            "appointment_status": self.appointment_status.value,
            "appointment_information": self.appointment_information,
            "patient": self.patient,
            "practitioner": self.practitioner
        }

    def display_appointment(self):
        return {
            "time": self.appointment_time,
            "status": self.appointment_status.value,
            "information": self.appointment_information,
            "patient": self.patient.patient_information,
            "practitioner": self.practitioner.practitioner_information
        }

    def retrieve_appointment(self):
        return {
            "appointment_time": self.appointment_time,
            "appointment_status": self.appointment_status.value,
            "appointment_information": self.appointment_information,
            "patient": self.patient.patient_information,
            "practitioner": self.practitioner.practitioner_information
        }




    def cancel_appointment(self):
        if self.appointment_status == AppointmentStatus.CANCELLED:
            raise ValueError("Appointment is already cancelled")

        self.appointment_status = AppointmentStatus.CANCELLED
        return self.display_appointment()

    @classmethod
    def get_patient_history(cls, patient):
        history = []

        for appointment in cls.appointments:
            if appointment.patient is patient:
                history.append(
                    appointment.display_appointment()
                )

        return history

if __name__ == "__main__":
    patient = Patient("John Smith")
    practitioner = Practitioner(
        "PR001",
        "Dr Brown",
        "General Practice"
    )

    appointment = Appointment(
        appointment_time="10:30",
        appointment_status=AppointmentStatus.BOOKED,
        appointment_information="General consultation",
        patient=patient,
        practitioner=practitioner
    )

    print(appointment.create_appointment())
    print(appointment.display_appointment())
    print(appointment.retrieve_appointment())

    try:
        duplicate = Appointment(
            appointment_time="10:30",
            appointment_status=AppointmentStatus.BOOKED,
            appointment_information="Another consultation",
            patient=patient,
            practitioner=practitioner
        )

        duplicate.create_appointment()

    except ValueError as error:
        print("Duplicate booking prevented:", error)


    # Test invalid appointment time
    try:
        invalid_appointment = Appointment(
            appointment_time="",
            appointment_status=AppointmentStatus.BOOKED,
            appointment_information="General consultation",
            patient=patient,
            practitioner=practitioner
        )

    except ValueError as error:
        print("Invalid appointment prevented:", error)

    second_appointment = Appointment(
        appointment_time="11:30",
        appointment_status=AppointmentStatus.BOOKED,
        appointment_information="Follow-up consultation",
        patient=patient,
        practitioner=practitioner
    )

    print("Second appointment:")
    print(second_appointment.create_appointment())

    print("Patient appointment history:")

    history = Appointment.get_patient_history(patient)

    for record in history:
        print(record)

    print("Cancelling appointment:")
    print(appointment.cancel_appointment())

    print("Updated appointment status:")
    print(appointment.display_appointment())

    try:
        appointment.cancel_appointment()
    except ValueError as error:
        print("Double cancellation prevented:", error)

    try:
        invalid_appointment = Appointment(
            appointment_time="12:30",
            appointment_status=AppointmentStatus.BOOKED,
            appointment_information="",
            patient=patient,
            practitioner=practitioner
        )
    except ValueError as error:
        print("Empty information prevented:", error)

    try:
        invalid_status = Appointment(
            appointment_time="13:30",
            appointment_status="Booked",
            appointment_information="Consultation",
            patient=patient,
            practitioner=practitioner
        )
    except TypeError as error:
        print("Invalid status prevented:", error)
