from datetime import datetime
# User Data Class
class UsersData:
    users = []
    def __init__(self, user_id:int, user_name:str, mail_id:str, phone_no:str, password:str):
        # Constructor for initializing user data
        self.user_id = user_id
        self.user_name = user_name
        self.mail_id = mail_id
        self.phone_no = phone_no
        self.password = password

# User Functionality Class
class UserFunctionality():
    # Method Overloading based on the type and number of parameters.
    def validate_user(self, mail_id, password=None):
        # Validate user based on mail_id and password
        registered_mail_id = [user.mail_id for user in UsersData.users if user.mail_id == mail_id]

        if registered_mail_id==[] and password==None:
            # If mail_id is not registered and no password provided, return True
            return True
        else:
            verified_password = [user.password for user in UsersData.users if user.password == password]
            if registered_mail_id and verified_password:
                # If mail_id is registered and password is verified, return True
                return True
        
    def signup(self):
        # User signup functionality
        user_id = (UsersData.users[-1].user_id)+1
        user_name = input("Enter User name:\n").lower()
        mail_id = input("Enter Mail Id:\n").lower()
        phone_no = input("Enter a Mobile number:\n")
        password = input("Enter a password:\n")

        if self.validate_user(mail_id):
            new_user = UsersData(user_id, user_name, mail_id, phone_no,password)
            UsersData.users.append(new_user)
            return mail_id

    def login(self):
        # User login functionality
        input_id = input("Enter your registered mail id:\n").lower()
        input_password = input("\nEnter your password:\n")

        if self.validate_user(input_id, input_password):
            return input_id


# Movie Data Class
class MoviesData:
    movies = []
    def __init__(self,movie_id:int, movie_name:str, duration:str, rating:float):
        # Constructor for initializing movie data
        self.movie_id = movie_id
        self.movie_name = movie_name
        self.duration = duration
        self.rating = rating

# Movie Functionality Class
class MovieFunctionality():
    # Method Overloading with same name but different behaviour.
    def display_info(self):
        # Display information about available movies
        print("--------------------------------------------------------\n")
        for movie in MoviesData.movies:
            print(movie.movie_id, '\t', movie.movie_name, '\t', movie.duration, '\t', movie.rating)

    def select_movie(self):
        # Select a movie based on user input
        movie_id = int(input("\nEnter a movie id:\n"))
        for movie in MoviesData.movies:
            if movie.movie_id == movie_id:
                return movie.movie_name

# Theatre Data Class
class TheatresData:
    theatres = []
    def __init__(self,theatre_id:int, theatre_name:str, location:str, rating:float, movies:list, show_time):
        # Constructor for initializing theatre data
        self.theatre_id = theatre_id
        self.theatre_name = theatre_name
        self.location = location
        self.rating = rating
        self.movies = movies
        self.show_time = show_time

# Theatre Functionality Class
class TheatreFunctionality():
    def display_info(self, movie):
        # Display information about available theatres showing a specific movie
        print("--------------------------------------------------------\n")
        for theatre in TheatresData.theatres:
            if movie in theatre.movies:
                print(theatre.theatre_id, '\t', theatre.theatre_name, '\t', theatre.location, '\t', theatre.rating)

    def select_theatre(self, selected_movie):
        # Select a theatre based on user input
        theatre_id = int(input("\nEnter a theatre id:\n"))
        for theatre in TheatresData.theatres:
            if theatre.theatre_id == theatre_id and selected_movie in theatre.movies:
                return theatre.theatre_name
    
    def display_showtime(self, selected_theatre):
        # Display showtime options for a selected theatre
        print("--------------------------------------------------------\n")
        for theatre in TheatresData.theatres:
            if theatre.theatre_name == selected_theatre:
                [print(show_id, show_time) for show_id, show_time in theatre.show_time.items()]
        return [theatre.show_time for theatre in TheatresData.theatres if theatre.theatre_name == selected_theatre]

    def select_showtime(self, selected_theatre):
        # Select a showtime based on user input
        show_time = self.display_showtime(selected_theatre)
        show_id = int(input("\nEnter the Show_id:\n"))
        print("--------------------------------------------------------\n")
        if show_id > 0 and show_id <= 4: 
            return show_time[0][show_id]  
        

# Seats Data Class
class SeatsData:
    seats_datas = []
    def __init__(self, theatre_name, movie, show_time):
        # Constructor for initializing seat data
        self.theatre_name = theatre_name
        self.movie = movie
        self.show_time = show_time
        self.seats = [["A1", "A2", "A3", "A4", "A5"], 
                      ["B1", "B2", "B3", "B4", "B5"], 
                      ["C1", "C2", "C3", "C4", "C5"],
                      ["D1", "D2", "D3", "D4", "D5"]]

# Seat Functionality Class
class SeatFunctionality:
    def display_seats(self, theatre_name, movie, show_time):
        # Display available seats for a selected theatre and showtime
        required_seats = [seat_details.seats for seat_details in SeatsData.seats_datas if seat_details.theatre_name == theatre_name and seat_details.movie == movie and seat_details.show_time == show_time]
        if required_seats == []:
            new_seats = SeatsData(theatre_name, movie, show_time)
            SeatsData.seats_datas.append(new_seats)
            self.display_seats(theatre_name, movie, show_time)

        else:
            for seat_details in SeatsData.seats_datas:
                if seat_details.theatre_name == theatre_name and seat_details.movie == movie and seat_details.show_time == show_time:
                    for rows in seat_details.seats:
                        print(*rows)

    
    def select_seats(self, theatre_name, movie, show_time):
        # Select seats based on user input
        self.display_seats(theatre_name, movie, show_time)
        required_seats = [seat_details.seats for seat_details in SeatsData.seats_datas if seat_details.theatre_name == theatre_name and seat_details.movie == movie and seat_details.show_time == show_time]            
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

# Bookings Data Class
class BookingsData:
    bookings = []
    def __init__(self, mail_id, selected_movie, selected_theatre, selected_show_time, selected_seats, total_price, payment_mode, booked_time):
        # Constructor for initializing booking data
        self.mail_id = mail_id
        self.movie = selected_movie
        self.theatre = selected_theatre
        self.show_time = selected_show_time
        self.seats = selected_seats
        self.price = total_price
        self.payment_mode = payment_mode
        self.booked_time = booked_time

# Booking Functionality Class
class BookingFunctionality:
    def booking_preview(self, mail_id, selected_movie, selected_theatre, selected_show_time, selected_seats, total_price):
        # Display booking preview and process payment
        print("--------------------------------------------------------\n")
        print("Booking Preview:\n")
        print(f'Movie Details: {selected_movie}')
        print(f'Theatre Name: {selected_theatre}')
        print(f'Show Details: {selected_show_time}')
        print(f'Seat details: {selected_seats}')
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
            booked_time = datetime.now().strftime("%y/%m/%d,%H:%M:%S")    
            new_booking = BookingsData(mail_id, selected_movie, selected_theatre, selected_show_time, selected_seats, total_price, payment_mode, booked_time)
            BookingsData.bookings.append(new_booking)
            return True

    def display_history(self):
        # Display booking history
        if len(BookingsData.bookings) == 0:
            print("Booking history is empty.")
        else:
            print("--------------------------------------------------------\n")
            for booking in BookingsData.bookings:
                    print(booking.movie, booking.theatre, booking.show_time, booking.seats, booking.price, booking.payment_mode, booking.booked_time, sep=' -- ')
    
    def delete_history(self):
        # Delete booking history
        if len(BookingsData.bookings) == 0:
            print("Booking history is empty.")
        else:
            BookingsData.bookings.pop()
            print("Your last history has been deleted")
            choice = input("\nDo you want to clear your all history? (y - to clear):\n")
            if choice.lower() ==  'y':
                BookingsData.bookings.clear()
                print("Booking history deleted successfully")
            else:
                print("Thank you")

# Movie Booking System Class
class MovieBookingSystem(UserFunctionality):

    def __init__(self):
        # Constructor for initializing Movie Booking System
        self.movie = MovieFunctionality()
        self.theatre = TheatreFunctionality()
        self.seats = SeatFunctionality()
        self.booking = BookingFunctionality()
        self.stay_in = True
        self.mail_id = None

    def signup_or_login(self):
        # Prompt user to signup or login
        choice = input("Enter a valid input(Signup/Login): \n").title()
        if choice == 'Signup':
            self.mail_id = self.signup()
            if not self.mail_id:
                print("User already exists.")
                self.stay_in = False

        elif choice == 'Login':
            self.mail_id = self.login()
            if not self.mail_id:
                print('Invalid mail id or password.')
                self.stay_in = False

    def run(self):
        # Main loop for Movie Booking System
        while self.stay_in:
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

    def book_movie (self):
        # Book a movie and initiate the booking process
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

        selected_seats = self.seats.select_seats(selected_theatre,selected_movie, selected_show_time)
        if not selected_seats:
            print("Invalid seat selection.")
            return

        total_price = len(selected_seats) * 200
        if not self.booking.booking_preview(self.mail_id, selected_movie, selected_theatre, selected_show_time, selected_seats, total_price):
            self.stay_in = False

    def display_booking_history(self):
        # Display booking history
        self.booking.display_history()

    def delete_booking_history(self):
        # Delete booking history
        self.booking.delete_history()

    def logout(self):
        # Logout the user from the system
        print("Logout Successfully.")
        self.stay_in = False

# Sample Data Initialization
if __name__ == '__main__':
    user1 = UsersData(1, 'anand46', 'anandkumar0962@gmail.com', '9876543210', 'anand0962')
    user2 = UsersData(2, 'hari13', 'hari13@gmail.com', '8765432109', 'hari13')
    user3 = UsersData(3, 'vigensh27', 'vignesh27@gmail.com', '7654321098', 'vignesh27')
    UsersData.users.append(user1)
    UsersData.users.append(user2)
    UsersData.users.append(user3)

    movie1 = MoviesData(1, 'Por Thozhil','2hr 27mins', 7.5)
    movie2 = MoviesData(2, 'Good Night','2hr 22mins', 7.7)
    movie3 = MoviesData(3, 'Leo       ','2hr 39mins', 8.1)
    MoviesData.movies.append(movie1)
    MoviesData.movies.append(movie2)
    MoviesData.movies.append(movie3)      

    theatre1 = TheatresData(1, 'PVR Cinemas   ', 'Anna Nagar', 7.5, ['Leo       ', 'Por Thozhil', 'Good Night'], {1:'10:30AM',2:'02:00PM',3:'06:20PM',4:'10:15PM'})
    theatre2 = TheatresData(2, 'AGS Cinemas   ', 'Villivakkam', 6.2, ['Leo       '], {1:'10:15AM',2:'01:45PM',3:'06:05PM',4:'09:45PM'})
    theatre3 = TheatresData(3, 'Rohini Cinemas', 'Koyambedu', 6.8, ['Leo       ','Good Night'], {1:'10:45AM',2:'02:15PM',3:'06:00PM',4:'10:05PM'})
    TheatresData.theatres.append(theatre1)
    TheatresData.theatres.append(theatre2)
    TheatresData.theatres.append(theatre3)

    booking_system = MovieBookingSystem()
    booking_system.signup_or_login()
    booking_system.run()

