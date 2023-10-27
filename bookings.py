from datetime import datetime
bookings = []

class Bookings:

    def __init__(self):

        self.bookings = bookings

    def booking_preview(self, mail_id, selected_movie, selected_theatre, selected_show_time, selected_seats, total_price):
        print("--------------------------------------------------------\n")
        print("Booking Preview:\n")
        print(f'Movie Details: {selected_movie}')
        print(f'Theatre Name: {selected_theatre}')
        print(f'Show Details: {selected_show_time}')
        print(f'Seat deatisl: {selected_seats}')
        print(f'Total amount: {total_price}')
        print("--------------------------------------------------------\n")
        print("Payment Options:\n1. Card\n2. UPI")
        payment_choice = int(input("\nChoose a payment option:\n"))
        print("--------------------------------------------------------\n")
        if payment_choice != 1 and payment_choice != 2:
            print("Invalid Payment method")
            return False
        else:
            if payment_choice == 1:
                payment_mode = "Card"
                print("Booked Successfully")
            elif payment_choice == 2:
                payment_mode = "UPI"
                print("Booked Successfully")
            booked_time=datetime.now().strftime("%y/%m/%d,%H:%M:%S")    
            booking_details = NewBooking(mail_id,selected_movie,selected_theatre,selected_show_time,selected_seats,total_price,payment_mode,booked_time)
            self.bookings.append(booking_details)
            return True

    def display_history(self):
        if len(self.bookings) == 0:
            print("Booking history is empty.")
        else:
            print("--------------------------------------------------------\n")
            for booking in self.bookings:
                    print(booking.movie,booking.theatre,booking.show_time,booking.seats,booking.price,booking.payment_mode,booking.booked_time,sep=' -- ')
    
    def delete_history(self):
        if len(self.bookings) == 0:
            print("Booking history is empty.")
        else:
            del(self.bookings[-1])
            print("Your last history has been deleted")
            choice = input("\nDo you clear your all history? (y/n):\n")
            if choice.lower() ==  'y':
                self.bookings.clear()

class NewBooking:

    def __init__(self,mail_id,selected_movie,selected_theatre,selected_show_time,selected_seats,total_price,payment_mode,booked_time):
        self.mail_id = mail_id
        self.movie = selected_movie
        self.theatre = selected_theatre
        self.show_time = selected_show_time
        self.seats = selected_seats
        self.price = total_price
        self.payment_mode = payment_mode
        self.booked_time = booked_time
