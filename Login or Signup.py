#Datas of the users.
users_data = [{"user_id":"anand0962@gmail.com","user_role": "admin","password":"anand0962"},{"user_id":"hari1302@gmail.com","user_role": "user","password":"hari1302"}]

#Datas of the movies and their information.
movies_list = [{"movie_id": "fastxmay2023", "movie_name": "Fast X", "duration":"141mins","rating":3.3},{"movie_id": "transformersmay2023", "movie_name": "Transformers: Rise of the Beats", "duration":"136mins","rating":3.7},{"movie_id": "spidermanmay2023", "movie_name": "Spider-Man: Across the Spider - Verse", "duration":"136mins","rating":4.6}]

#Class Register for login and signup functionalities.
class Register:
    
    #Constructor
    def __init__(self,user_id,user_role, password): #declaration of instance attributes.
        self.user_id    = user_id
        self.user_role = user_role
        self.password = password
    
    def login(self):
        #Using list comprehension method to validate the user.
        check = [d for d in users_data if d["user_id"] in self.user_id and d["user_role"] in self.user_role and d["password"] in self.password]
        
        if check !=[]:
            return "Login success."
            
        else:
            return "Invalid data(s)."
            
    def signup(self):
        #Using list comprehension method to validate the user.
        check = [d for d in users_data if d["user_id"] in self.user_id]
        
        if check !=[]:
            return "Mail id already exist."
            
        #Validating the new users input datas using string methods    
        elif (self.user_id[0]).isalpha() and (self.user_id).endswith(".com") and (self.user_role == 'admin' or self.user_role == 'user'):
            new_user = {"user_id":self.user_id,"user_role":self.user_role,"password":self.password}
            
            #Adding the new user's data to the list of users data using append() method
            users_data.append(new_user)
            print(users_data)
            return "Signup Success."
            
        else:
            return "Invalid Mail Id or Invalid user role."

#Movies_Info class to display the movies information to the user.
class Movies_Info(Register): 

#Methods and properties of Register class were inherited through single inheritance.
               
    #constructor
    def __init__(self,user_id,user_role,password):
        #inherting the Register class's instance attributes through super() method
        super().__init__(user_id,user_role,password)
        
        #Displaying movies information.
    def display_movies(self):
           for movie in movies_list:
                 print("Movie Name:",movie["movie_name"], "-" ,"Duration:",movie["duration"], "-" ,"Rating:",movie["rating"])
                                  
if __name__ == "__main__":
    ch = int(input("Enter your choice:\n 1.Login\n 2.Signup\n"))
    
    if ch ==1:
        user_id = input("Enter the mail id:\n")
        user_role = input("Enter your choice:\n 1.user\n 2.admin\n")
        password = input("Enter the password:\n")
        
        #Creating Instance for Register class
        obj = Register(user_id,user_role, password)
        #Calling login() instance method to validate the input datas
        info = obj.login()
        print(info)
        
    elif ch ==2:
        user_id = input("Enter a mail id:\n")
        user_role = input("Enter your choice:\n 1.user\n 2.admin\n")
        password = input("Enter  password:\n")
        #Creating Instance for Register class
        obj = Register(user_id,user_role, password)
        #Calling signup() instance method to validate the input datas and add the datas to the users_data list.
        info =obj.signup()
        print(info)
        
    else:
        print("Invalid input")
    if info == "Signup Success." or info == "Login success.":
        ch2 = int(input("Enter your choice:\n 1.Movies list.\n"))
    
        if ch2 == 1:            
            movies =  Movies_Info(user_id,user_role,password )
            movies.display_movies()
        
      