# Task 1
# Create and run a simple Python file with basic input/output statements

print("Welcome to SmartCare: Community Clinic Appointment Booking System!")

# First Appointment
patient1_name = "Alice Smith"
practitioner1_name = "Dr. John Doe"
appointment1_time = "2024-07-20 10:00 AM"

print(f"Patient: {patient1_name} | Practitioner: {practitioner1_name} | Time: {appointment1_time}")

# Second Appointment
patient2_name = "Bob Johnson"
practitioner2_name = "Dr. Jane Roe"
appointment2_time = "2024-07-20 11:30 AM"

print(f"Patient: {patient2_name} | Practitioner: {practitioner2_name} | Time: {appointment2_time}")


# Task 1 Enhanced
# Use lists, dictionaries and functions to enhance the Python file

appointments = []


def book_appointment(patient_name, practitioner_name, appointment_time):

    # Check that patient name is not empty
    if not patient_name:
        raise ValueError("Patient name cannot be empty")

    # Part G improvement:
    # Prevent a practitioner from being booked at the same time
    for appointment in appointments:
        if (
            appointment["practitioner"] == practitioner_name
            and appointment["time"] == appointment_time
        ):
            raise ValueError("Practitioner is already booked at this time")

    appointment = {
        "patient": patient_name,
        "practitioner": practitioner_name,
        "time": appointment_time
    }

    appointments.append(appointment)


def display_appointments():

    if not appointments:
        print("No appointments recorded.")
        return

    for appointment in appointments:
        print(
            f"Patient: {appointment['patient']} | "
            f"Practitioner: {appointment['practitioner']} | "
            f"Time: {appointment['time']}"
        )


print("\nWelcome to SmartCare: The Clinical Appointment Booking System!")

book_appointment(
    "Alice Smith",
    "Dr. John Doe",
    "2024-07-20 10:00 AM"
)

book_appointment(
    "Bob Johnson",
    "Dr. Jane Roe",
    "2024-07-20 11:30 AM"
)

display_appointments()


# Part F - Edge Case Testing

print("\n--- Edge Case Testing ---")

# Test 1: Normal input
print("\nTest 1: Normal input")

try:
    book_appointment(
        "Charlie Brown",
        "Dr. John Doe",
        "2024-07-20 12:00 PM"
    )
    print("Appointment added successfully.")
except ValueError as error:
    print("Error:", error)


# Test 2: Blank patient name
print("\nTest 2: Blank patient name")

try:
    book_appointment(
        "",
        "Dr. Jane Roe",
        "2024-07-20 1:00 PM"
    )
except ValueError as error:
    print("Error:", error)


# Test 3: Duplicate practitioner and time
print("\nTest 3: Duplicate practitioner and time")

try:
    book_appointment(
        "David Lee",
        "Dr. John Doe",
        "2024-07-20 10:00 AM"
    )
except ValueError as error:
    print("Error:", error)


# Test 4: None input
print("\nTest 4: None input")

try:
    book_appointment(
        None,
        "Dr. Jane Roe",
        "2024-07-20 2:00 PM"
    )
except ValueError as error:
    print("Error:", error)