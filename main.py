from users import UserData
from movies import MoviesData
from theatres import TheatresData
from seats import SeatsData
from bookings import NewBooking

class MovieBookingSystem:
    def __init__(self):
        self.user = UserData()
        self.movie = MoviesData()
        self.theatre = TheatresData()
        self.seats = SeatsData()
        self.booking = NewBooking()
        self.stay_in = True
        self.mail_id = None

    def signup_or_login(self):
        choice = input("Enter a valid input (Signup / Login):\n").title()
        if choice == 'Signup':
            self.mail_id = self.user.signup()
            if not self.mail_id:
                print("User already exists.")
                self.stay_in = False
        elif choice == 'Login':
            self.mail_id = self.user.login()
            if not self.mail_id:
                print('Invalid mail id or password.')
                self.stay_in = False

    def book_movie(self):
        self.movie.display_info()
        selected_movie = self.movie.select_movie()
        if not selected_movie:
            print("Invalid movie id.")
            return

        self.theatre.display_info(selected_movie)
        selected_theatre = self.theatre.select_theatre(selected_movie)
        if not selected_theatre:
            print("Invalid theatre id.")
            return

        selected_show_time = self.theatre.select_showtime(selected_theatre)
        if not selected_show_time:
            print("Invalid show id.")
            return

        selected_seats = self.seats.select_seats(selected_theatre, selected_show_time)
        if not selected_seats:
            print("Invalid seat selection.")
            return

        total_price = len(selected_seats) * 200
        if not self.booking.booking_preview(self.mail_id, selected_movie, selected_theatre, selected_show_time, selected_seats, total_price):
            self.stay_in = False

    def display_booking_history(self):
        self.booking.display_history()

    def delete_booking_history(self):
        self.booking.delete_history()

    def logout(self):
        print("Logout Successfully.")
        self.stay_in = False

    def run(self):
        while self.stay_in:
            if self.mail_id:
                print("--------------------------------------------------------\n")
                print("Menu:")
                print("1. Book Movie")
                print("2. Display Booking history")
                print("3. Delete Booking history")
                print("4. Logout")
                choice = int(input("\nEnter your choice:\n"))
                if choice == 1:
                    self.book_movie()
                elif choice == 2:
                    self.display_booking_history()
                elif choice == 3:
                    self.delete_booking_history()
                elif choice == 4:
                    self.logout()
                else:
                    print("Invalid Choice")

if __name__ == "__main__":
    booking_system = MovieBookingSystem()
    booking_system.signup_or_login()
    booking_system.run()