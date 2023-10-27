from users import Users
from movies import Movies
from theatres import Theatres
from seats import Seats
from bookings import Bookings

user = Users()
movie = Movies()
theatre = Theatres()
seats = Seats()
booking = Bookings()


stay_in = True
mail_id = None

choice = input("Enter a valid input (Signup / Login):\n").title()
if choice == 'Signup':
    mail_id = user.signup()
    if not mail_id:
        print("User already exists.")
        stay_in = False
elif choice == 'Login':
    mail_id = user.login()
    if not mail_id:
        print('Invalid mail id or password.')
        stay_in = False

while stay_in:
    if mail_id:
        print("--------------------------------------------------------\n")
        print("1. Book Movie")
        print("2. Display Booking history")
        print("3. Delete Booking history")
        print("4. Logout")
        choice = int(input("\nEnter your choice:\n"))
        if choice == 1:
            selected_movie = movie.select_movie()
            if selected_movie:
                selected_theatre = theatre.select_theatre(selected_movie)
                if selected_theatre:  
                    selected_show_time = theatre.select_showtime(selected_theatre)
                    if selected_show_time:
                        selected_seats=seats.select_seats(selected_theatre, selected_show_time)
                        if selected_seats:
                            total_price = len(selected_seats)*200
                            if not booking.booking_preview(mail_id, selected_movie, selected_theatre, selected_show_time, selected_seats, total_price):
                                stay_in = False
                        else:
                            print("Invalid seat selection.")
                            stay_in = False
                    else:
                        print("Invalid show id.")
                        stay_in = False
                else:
                    print("Invalid theatre id.")
                    stay_in = False      
            else:
                print("Invaild movie id.")
                stay_in = False

        if choice == 2:
            booking.display_history()

        if choice == 3:
            booking.delete_history()

        if choice<1 or choice>= 4:
            print("Logout Successfully.")
            stay_in = False