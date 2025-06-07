class Schedule:
    def __init__(self, time, desc):
        self.time = time
        self.desc = desc

    def __str__(self):
        return f"{self.time} - {self.desc}"


class Attendee:
    def __init__(self, a_id, a_name, a_company, a_feedback=None):
        self.a_id = a_id
        self.a_name = a_name
        self.a_company = a_company
        self.a_feedback = a_feedback

    def __str__(self):
        feedback = self.a_feedback if self.a_feedback else "No Feedback is mentioned"
        return f"Id: {self.a_id}, Name: {self.a_name}, Company: {self.a_company}, Feedback: {feedback}"

    def set_feedback(self, feedback):
        self.a_feedback = feedback


class Event:
    def __init__(self, e_id, e_name, e_start, e_end):
        self.e_id = e_id
        self.e_name = e_name
        self.e_start = e_start
        self.e_end = e_end
        self.schedule = []
        self.attendees = []

    def __str__(self):
        output = f"Event Details for: {self.e_id}\n"
        output += f"Event Name: {self.e_name}\n"
        output += f"Starting at: {self.e_start}\n"
        output += f"Ending at: {self.e_end}\n"

        if not self.schedule:
            output += "There are no schedules added.\n"
        else:
            output += "Event Schedules:\n"
            for schedule in self.schedule:
                output += f"  {schedule}\n"

        if not self.attendees:
            output += "No attendees registered for this event.\n"
        else:
            output += "Event Attendees:\n"
            for attendee in self.attendees:
                output += f"  {attendee}\n"
        return output

    def add_schedule(self, time, desc):
        schedule = Schedule(time, desc)
        self.schedule.append(schedule)

    def add_attendee(self, id, name, company, feedback=None):
        attendee = Attendee(id, name, company, feedback)
        self.attendees.append(attendee)


# Dictionary to hold events
events = {}

# Create Event
def create_event(id, name, start, end):
    if id not in events:
        event = Event(id, name, start, end)
        events[id] = event
        print(f"Event {name} created successfully.\n")
    else:
        raise Exception("Event Already Exists..")

# Show all events
def show_events():
    for e_id in events:
        print(events[e_id])


# ---------- Test ----------
create_event("E_4Y5", "Developer Camp", "04/05/2025", "06/05/2025")

# Add sample schedule and attendee
events["E_4Y5"].add_schedule("10:00 AM", "Welcome Speech")
events["E_4Y5"].add_attendee("A_123", "Alice", "TCS", "Very engaging")

# Display all events
show_events()
