#Parking Garage Project

class Parking_Garage():


    def __init__(self, tickets):
        self.tickets = []
        self.spaces_available = []
        self.current_tickets = {}

    def take_ticket(self):
        if self.spaces_available <= 0:
            print("This lot is full.")
        else:
            self.spaces_available -= self.tickets
            new_ticket = self.current_tickets += 1
            


    def pay(self):
        ticket_number = input("What is your ticket number?")
        



    def leave():


