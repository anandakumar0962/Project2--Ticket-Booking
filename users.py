users = []
class Users:

    def __init__(self):
        self.users = users

    def login(self):
        print("--------------------------------------------------------\n")
        input_id = input("Enter your registered mail id:\n").lower()
        input_password = input("\nEnter your password:\n")
        registered_mail_id = [user.mail_id for user in self.users if user.mail_id == input_id]
        verified_password = [user.password for user in self.users if user.password == input_password]
        if registered_mail_id and verified_password:
            return input_id
        
    def signup(self):
        user_id = (self.users[-1].user_id)+1
        print("--------------------------------------------------------\n")
        user_name = input("Enter User name:\n").lower()
        mail_id = input("Enter Mail Id:\n").lower()
        phone_no = input("Enter a  Mobile number:\n")
        password = input("Enter a password:\n")
        registered_mail_id = [user.mail_id for user in self.users if user.mail_id == mail_id]
        if not registered_mail_id:
            new_user = NewUser(user_id, user_name, mail_id, phone_no,password)
            self.users.append(new_user)
            return mail_id


class NewUser:

    def __init__(self, user_id:int, user_name:str, mail_id:str, phone_no:str, password:str):
        self.user_id = user_id
        self.user_name = user_name
        self.mail_id = mail_id
        self.phone_no = phone_no
        self.password = password


user1 = NewUser(1, 'anand46', 'anandkumar0962@gmail.com', '9876543210', 'anand0962')
user2 = NewUser(2, 'hari13', 'hari13@gmail.com', '8765432109', 'hari13')
user3 = NewUser(3, 'vigensh27', 'vignesh27@gmail.com', '7654321098', 'vignesh27')
users.append(user1)
users.append(user2)
users.append(user3)