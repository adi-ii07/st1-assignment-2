# SmartCare Requirements – Stage 2

## Client Brief Analysis

SmartCare currently uses spreadsheets and paper records to manage patient and appointment information. This has created several problems, including duplicate appointment bookings, difficulty finding patient information, inconsistent appointment statuses, and limited appointment history.

The proposed system will provide a small and maintainable way to manage patients, practitioners, and appointments.

## Stakeholders

| Stakeholder | Interest in the System |
|---|---|
| Patients | Their personal information and appointments are managed by the system. |
| Practitioners | Their appointments and patient bookings need to be managed. |
| Staff | They need to access patient information and manage appointments. |
| Management | They need a system that is useful and maintainable. |

## Scope

### In Scope

- Store patient information
- Store practitioner information
- Create and manage appointments
- View patient information
- Maintain appointment history
- Record appointment statuses
- Reduce duplicate appointment bookings

### Out of Scope

- Online payments
- Video consultations
- Mobile application
- Automatic SMS or email reminders
- Integration with external medical systems

### Provisional / Requires Clarification

- Whether patients can book their own appointments
- Whether appointments can be cancelled or rescheduled
- Whether different staff members require different access permissions
- How long appointment history should be retained

## Functional Requirements

**FR-01:** The system shall allow staff to create a patient record.

**FR-02:** The system shall allow staff to view patient information.

**FR-03:** The system shall allow practitioner information to be stored.

**FR-04:** The system shall allow appointments to be created for a patient and practitioner.

**FR-05:** The system shall display appointment information.

**FR-06:** The system shall prevent duplicate appointment bookings for the same practitioner at the same time.

**FR-07:** The system shall store the status of an appointment.

**FR-08:** The system shall allow appointment information to be retrieved.

**FR-09:** The system shall maintain appointment history.

**FR-10:** The system shall associate each appointment with the relevant patient and practitioner.

## Non-Functional Requirements

**NFR-01 – Usability:** The system should be simple and easy for staff to understand and use.

**NFR-02 – Maintainability:** The system should be organised so that changes can be made without unnecessarily affecting other parts of the system.

**NFR-03 – Data Integrity:** The system should maintain consistent patient, practitioner, and appointment information.

**NFR-04 – Reliability:** The system should reliably store and retrieve appointment information.

**NFR-05 – Testability:** Individual system functions should be able to be tested to check that they produce the expected results.

## User Stories and Acceptance Criteria

### User Story 1 – Create an Appointment

**As a staff member, I want to create an appointment for a patient with a practitioner so that the appointment can be recorded.**

Acceptance Criteria:

- Given a patient and practitioner are available, when staff create an appointment, then the appointment should be stored.
- Given valid appointment information is entered, when the appointment is created, then it should be linked to the correct patient and practitioner.
- Given an appointment has been successfully created, when staff view the appointment, then the appointment information should be displayed.

### User Story 2 – View Patient Information

**As a staff member, I want to view patient information so that I can quickly find the information I need.**

Acceptance Criteria:

- Given a patient record exists, when staff access the patient record, then the stored patient information should be displayed.
- Given multiple patient records exist, when staff select a patient, then the information for the selected patient should be displayed.
- Given the requested patient record does not exist, when staff attempt to access it, then the system should indicate that the patient cannot be found.

### User Story 3 – Prevent Duplicate Bookings

**As a staff member, I want the system to prevent duplicate practitioner bookings so that a practitioner is not booked twice at the same time.**

Acceptance Criteria:

- Given a practitioner is available, when an appointment is created for a free time, then the appointment should be stored.
- Given a practitioner already has an appointment at a particular time, when another appointment is created for the same practitioner at the same time, then the system should reject the booking.
- Given a duplicate booking is rejected, when staff receive the result, then the system should indicate that the practitioner is already booked.

### User Story 4 – View Appointment History

**As a staff member, I want to view appointment history so that previous appointments can be accessed.**

Acceptance Criteria:

- Given a patient has previous appointments, when staff view the patient's appointment history, then the previous appointments should be displayed.
- Given multiple previous appointments exist, when the history is viewed, then the stored appointments should be available.
- Given no previous appointments exist, when staff view the appointment history, then the system should indicate that no appointment history is available.

### User Story 5 – Appointment Status

**As a staff member, I want appointments to have a consistent status so that I can understand their current state.**

Acceptance Criteria:

- Given an appointment exists, when its information is viewed, then its status should be displayed.
- Given an appointment status is stored, when the appointment is retrieved, then the same status should be shown.
- Given appointment information is maintained, when its status is recorded, then the system should store the status consistently.

## AI Requirements Review

AI was used to review the SmartCare requirements for ambiguity, missing information, inconsistencies, and testability issues.

| AI Suggestion | Finding |
|---|---|
| Clarify who can create appointments | The client brief refers to staff but does not specify which staff members can create or manage appointments. |
| Define appointment statuses | The client brief identifies inconsistent appointment statuses as a problem but does not specify what statuses should be available. |
| Clarify duplicate booking rules | Duplicate bookings are identified as a problem, but the exact conditions that make a booking a duplicate need clarification. |
| Define patient information | The client brief refers to patient information but does not specify exactly what patient details need to be stored. |
| Define appointment history | Appointment history is required, but the brief does not specify how long appointment history should be retained. |
| Improve measurable NFRs | Some non-functional requirements use terms such as "simple" and "reliably", which may need measurable criteria to make them easier to test. |

## Verification of AI Suggestions

| AI Suggestion | Decision | Reason |
|---|---|---|
| Clarify who can create appointments | Unverified | The client brief mentions staff but does not define specific staff permissions. |
| Define appointment statuses | Accepted | Inconsistent appointment status is directly identified as a current problem. |
| Clarify duplicate booking rules | Accepted | Duplicate bookings are identified as a problem, but the exact rule needs clarification. |
| Define patient information | Accepted | Patient information is mentioned, but the required information is not specified. |
| Define appointment history | Unverified | Appointment history is required, but no retention period is provided. |
| Improve measurable NFRs | Accepted | Making the requirements measurable would make them easier to test. |

## Assumptions and Open Questions

### Assumptions

- The SmartCare system will primarily be used by clinic staff.
- Each appointment is linked to one patient and one practitioner.
- A practitioner cannot have two appointments at the same time.
- Appointment information will include the patient, practitioner, time and status.
- Patient, practitioner and appointment information will be stored by the system.

### Open Questions

- Which staff members should be allowed to create or manage appointments?
- What appointment statuses should be available?
- What specific patient information needs to be stored?
- Should appointments be able to be cancelled or rescheduled?
- How long should appointment history be retained?
- Do different staff members need different access permissions?

## Reflection

During Stage 2, I learned that requirements analysis is important because a client brief does not always provide every detail needed to develop a system. I identified the main requirements for the SmartCare system and separated them into functional and non-functional requirements. I also created user stories and acceptance criteria, which helped me understand how requirements can be written from the user's perspective and how they can later be tested.

I used AI to review my requirements and identify possible ambiguities, missing information and areas that required clarification. The AI suggested issues such as unclear staff permissions, undefined appointment statuses, duplicate booking rules and unspecified patient information. I then compared these suggestions with the client brief instead of automatically accepting them. This helped me understand that AI can assist with requirements analysis, but its suggestions still need to be checked against the original source.

This stage also showed me how requirements can change as more information becomes available. Keeping assumptions and open questions separate makes it easier to identify what still needs to be confirmed before development. Overall, Stage 2 helped me better understand requirements engineering, user stories, acceptance criteria and the importance of reviewing AI-generated suggestions.

