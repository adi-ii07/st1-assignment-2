# Stage 4 – AI Engineering Log

**AI contribution:** AI was used to help implement and review the Appointment class, including validation, booking conflicts and cancellation behaviour.

**Changes made:** I reviewed the generated code and added type hints and input validation. I also checked that cancelled appointments remained in the system and that repeated cancellations were rejected.

**Verification:** I tested valid appointments, duplicate bookings, invalid information, invalid status values and repeated cancellations. The program completed successfully with exit code 0.

## Reflection

I modified the Appointment implementation to improve validation and make the code more consistent. The approved UML helped limit the implementation to the required classes and relationships rather than introducing unnecessary features. I reviewed the code and tested its behaviour instead of relying only on AI-generated suggestions.

## AI Prompt
Act as a Python pair programmer. Implement only the Appointment class from the approved SmartCare UML.
Use type hints and an AppointmentStatus enum. Cancelled appointments remain as objects. Do not add
database, UI, notification or service classes. Protect status transitions and explain any decision not directly
visible in the UML.
