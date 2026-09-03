AI Usage Record

Part C - AI review

AI Tool Used: Microsoft Copilot

promt:
I asked Microsoft Copilot to review my SmartCare appointment booking code, explain what the code does, identify limitations, and suggest possible improvements.

AI feedback:
Copilot identified the following limitations:
- The program uses a global appointments list, which can make the code harder to test and reuse.
- The practitioner name and appointment time are not properly validated.
- The program does not check for appointment conflicts, meaning a practitioner could be double-booked.

Copilot suggested the following improvements:
- Encapsulate the appointment data instead of relying on global state.
- Add input validation.
- Check for duplicate or conflicting appointments.
- Use return values instead of only printing information.

my evaluation:
I agree that input validation and conflict detection would make the system more reliable. The current program works for simple appointment bookings, but it does not prevent incorrect information or double bookings. I also understand that reducing the use of global data could make the program easier to maintain.