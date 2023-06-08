# Datas of the users.
users_data = [{"user_id":"anand0962@gmail.com","user_role": "admin","password":"anand0962"},{"user_id":"hari1302@gmail.com","user_role": "user","password":"hari1302"}]

# Datas of the movies and their information.
movies_list = [{"movie_id": 1, "movie_name": "Fast X", "duration":"141mins","rating":3.3},{"movie_id": 2, "movie_name": "Transformers: Rise of the Beats", "duration":"136mins","rating":3.7},{"movie_id": 3, "movie_name": "Spider-Man: Across the Spider - Verse", "duration":"136mins","rating":4.6}]

# Datas of the theatre's information.
theatres_details = [{"movie_name": "Fast X","theatres":[{"theatre_id":4,"theatre_name":"PVR Sathyam Cinemas", "show_time":["10:30AM", "02:00PM", "06:30PM", "10:30PM"],"theatre_rating": 4.0},{"theatre_id":2,"theatre_name":"Kasi Talkies", "show_time":["10:00AM", "01:30PM", "06:15PM", "10:00PM"],"theatre_rating": 3.8}]},{"movie_name": "Transformers: Rise of the Beats","theatres":[{"theatre_id":3,"theatre_name":"Sangam Cinemas", "show_time":["10:00AM", "01:00PM", "06:00PM", "10:00PM"],"theatre_rating": 4.2},{"theatre_id":1,"theatre_name":"Jazz Cinemas", "show_time":["10:45AM", "02:15PM", "06:00PM", "10:00PM"],"theatre_rating": 4.5}]},{"movie_name": "Spider-Man: Across the Spider - Verse","theatres":[{"theatre_id":2,"theatre_name":"Kasi Talkies", "show_time":["10:00AM", "01:30PM", "06:15PM", "10:00PM"],"theatre_rating": 3.8},{"theatre_id":1,"theatre_name":"Jazz Cinemas", "show_time":["10:45AM", "02:15PM", "06:00PM", "10:00PM"],"theatre_rating": 4.5},{"theatre_id":4,"theatre_name":"PVR Sathyam Cinemas", "show_time":["10:30AM", "02:00PM", "06:30PM", "10:30PM"],"theatre_rating": 4.0},{"theatre_id":3,"theatre_name":"Sangam Cinemas", "show_time":["10:00AM", "01:00PM", "06:00PM", "10:00PM"],"theatre_rating": 4.2}]}]


# Class Register for login and signup functionalities.
class Register:
    
    # Constructor
    def __init__(self,user_id,user_role, password): # declaration of instance attributes.
        self.user_id    = user_id
        self.user_role = user_role
        self.password = password
    
    def login(self):
        # Using list comprehension method to validate the user.
        check = [d for d in users_data if d["user_id"] == self.user_id and d["user_role"] == self.user_role and d["password"] == self.password]
        
        if check !=[]:
            return "Login success."
            
        else:
            return "Invalid data(s)."
            
    def signup(self):
        # Using list comprehension method to validate the user.
        check = [d for d in  users_data if d["user_id"] == self.user_id]
        
        if check !=[]:
            return "Mail id already exist."
            
        # Validating the new users input datas using string methods    
        elif (self.user_id[0]).isalpha() and (self.user_id).endswith(".com") and (self.user_role == 'admin' or self.user_role == 'user'):
            new_user = {"user_id":self.user_id,"user_role":self.user_role,"password":self.password}
            
            # Adding the new user's data to the list of users data using append() method
            users_data.append(new_user)
            print(users_data)
            return "Signup Success."
            
        else:
            return "Invalid Mail Id or Invalid user role."

# Movies_Info class to display the movies information to the user.

class Movies_Info():         
        # Displaying movies information.
    def display_movies(self): 
              
        for movie in movies_list:
            print(movie["movie_id"],'.',"Movie Name:",movie["movie_name"],'\n',"Duration:",movie["duration"], "\n" ,"Rating:",movie["rating"])
            print("-------------------------")
                 
                 
# Class Theatres_Info to show the theatres available for the choosen movie.

class Theatres_Info():
    
    def __init__(self,selected_movie):  
        self.selected_movie = selected_movie
        
 # Displaying the theatres based on the movie selected using lambda function along with filter() function.   
  
    def display_theatres(self):
        theatres = list(filter(lambda x: x["movie_name"] == self.selected_movie, theatres_details))
        print("\nSelected movie:\n", self.selected_movie)
        for i in theatres[0]["theatres"]:
            print("Theatre Name:",i["theatre_name"],"\nShow Time:", i["show_time"],"\nRating:", i["theatre_rating"])
            print("----------------------------")
                                             
if __name__ == "__main__":
    choice = int(input("Enter your choice:\n 1.Login\n 2.Signup\n"))
    
    if choice ==1:
        user_id = input("\nEnter the mail id:\n")
        user_role = input("\nEnter your role:\n 1.user\n 2.admin\n")
        password = input("\nEnter the password:\n")
        
        # Creating Instance for Register class
        object = Register(user_id,user_role, password)
        # Calling login() instance method to validate the input datas
        validation = object.login()
        print(validation)
        
    elif choice ==2:
        user_id = input("\nEnter a mail id:\n")
        user_role = input("\nEnter your choice:\n 1.user\n 2.admin\n")
        password = input("\nEnter  password:\n")
        # Creating Instance for Register class
        object = Register(user_id,user_role, password)
        # Calling signup() instance method to validate the input datas and add the datas to the users_data list.
        validation =object.signup()
        print(validation)
        
    else:
        print("Invalid input\n")
    if  validation == "Signup Success." or validation == "Login success.":
        print("\nList of movies running now\n")
        
        # Creating a movies instance for Movies_Info class.       
        movies =  Movies_Info()
        # Displaying the list of movies running in theatres.
        movies.display_movies()
        # Getting a movie selected from the user
        movie_choice = int(input("\nSelect the movie to see theatres:\n"))
        movie_info = [d for d in movies_list if d["movie_id"] == movie_choice]
        if movie_info !=[]:
            
            selected_movie = movie_info[0]["movie_name"]
            # Creating instance for Theatres_Info class
            theatre_obj= Theatres_Info(selected_movie)
            # Displaying the theatres and its details based on the movie selected.
            theatre_obj.display_theatres()
        else:
         print("Invalid movie choice.")
         ying the theatres and its details based on the movie selected.
        theatre_obj.display_theatres()
         