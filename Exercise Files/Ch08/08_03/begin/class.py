class Attendee:
    'Common base class for all attendees'

    def __init__(self, name, tickets):
        self.name = name
        self.tickets = tickets

    def displayAttendee(self):
        print('Name : {}, Tickets: {}'.format(self.name, self.tickets))

    def addTicket(self):
        self.tickets += 1
        print('{} tickets increased to {}'.format(self.name, self.tickets))

print("-------------------------------")
Attendee1=Attendee('Ali',2)
Attendee2=Attendee('Ola',3)

# Attendee.displayAttendee(Attendee1)
# Attendee.addTicket(Attendee1)

# Attendee.displayAttendee(Attendee2)
# Attendee.addTicket(Attendee2)

Attendee1.displayAttendee()
Attendee2.displayAttendee()
Attendee1.addTicket()
Attendee2.addTicket()



print("-------------------------------")
