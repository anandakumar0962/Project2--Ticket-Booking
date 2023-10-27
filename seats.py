seats_datas = []
class Seats:
    def __init__(self):
        self.seats = seats_datas

    def display_seats(self, theatre_name, show_time):
        required_seats = [seat_details.seats for seat_details in self.seats if seat_details.theatre_name == theatre_name and seat_details.show_time == show_time]
        if required_seats == []:
            new_seats = NewSeats(theatre_name, show_time)
            self.seats.append(new_seats)
            self.display_seats(theatre_name, show_time)
        else:
            for seat_deatils in self.seats:
                if seat_deatils.theatre_name == theatre_name and seat_deatils.show_time == show_time:
                    for rows in seat_deatils.seats:
                        print(*rows)
    
    def select_seats(self, theatre_name, show_time):
        self.display_seats(theatre_name, show_time)
        required_seats = [seat_details.seats for seat_details in self.seats if seat_details.theatre_name == theatre_name and seat_details.show_time == show_time]            
        requested_seats = input("\nEnter the seats as space separated to select:(Ex. A1 A2 B2)\n").upper().split(' ')
        selected_seats = []
        for rows in required_seats[0]:
            for seat in rows:
                if seat in requested_seats:
                    selected_seats.append(seat)
        if len(selected_seats) == len(requested_seats):
            for rows in required_seats[0]:
                for i in range(len(rows)):
                    if rows[i] in selected_seats:
                        rows[i] = '0 '
            return selected_seats
class NewSeats:

    def __init__(self, theatre_name, show_time):
        self.theatre_name = theatre_name
        self.show_time = show_time
        self.seats = [["A1", "A2", "A3", "A4", "A5"], 
                      ["B1", "B2", "B3", "B4", "B5"], 
                      ["C1", "C2", "C3", "C4", "C5"],
                      ["D1", "D2", "D3", "D4", "D5"]]

