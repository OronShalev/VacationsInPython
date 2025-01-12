from datetime import datetime, date
import re
from source.Logic.User_Logic import UserLogic

class UserFacade:
    def __init__(self):
        self.params = []
        self.now = date.today()
        self.logic = UserLogic()
        
    def logout_user(self):
        self.params = []

    def login_user(self):
        print("\n\nLogin\n")
        self.logout_user()
        self.get_email_exists()
        self.get_password_matched()
        
    def register_user(self):
        print("\n\nRegister\n")
        self.logout_user()
        self.get_first_name()
        self.get_last_name()
        self.get_email()
        self.get_password()
        self.get_date_of_birth()

        success = self.logic.add_user(*self.params)
        if success:
            print("User registered successfully!")
        else:
            print("User registration failed. Email might already exist.")

    def get_first_name(self):
        while True:
            first_name = input("Enter first name: ").strip()
            if not first_name.isalpha():
                print("First name must contain only letters.")
            elif len(first_name) < 2:
                print("First name must be at least 2 characters long.")
            else:
                self.params.append(first_name)
                print("First name added.")
                break

    def get_last_name(self):
        while True:
            last_name = input("Enter last name: ").strip()
            if not last_name.isalpha():
                print("Last name must contain only letters.")
            elif len(last_name) < 2:
                print("Last name must be at least 2 characters long.")
            else:
                self.params.append(last_name)
                print("Last name added.")
                break

    def get_email(self):
        while True:
            email = input("Enter email: ").strip()
            email_pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
            if not re.match(email_pattern, email):
                print("Invalid email format.")
            else:
                self.params.append(email)
                print("Email added.")
                break

    def get_password(self):
        while True:
            password = input("Enter password: ").strip()
            password_pattern = r'^(?=.*[A-Za-z])(?=.*\d)[A-Za-z\d]{6,}$'  # Minimum 6 characters, at least 1 letter and 1 number
            if not re.match(password_pattern, password):
                print("Password must be at least 6 characters long and include at least one letter and one number.")
            else:
                self.params.append(password)
                print("Password added.")
                break

    def get_date_of_birth(self):
        while True:
            try:
                date_str = input("Enter date of birth (YYYY-MM-DD): ").strip()
                date_of_birth = datetime.strptime(date_str, "%Y-%m-%d").date()

                if date_of_birth >= self.now:
                    print("Date of birth cannot be in the future.")
                elif (self.now - date_of_birth).days / 365.25 < 18:
                    print("User must be at least 18 years old.")
                else:
                    self.params.append(date_of_birth)
                    print("Date of birth added.")
                    break
            except ValueError:
                print("Invalid date format. Please use YYYY-MM-DD.")

    def get_email_exists(self):
        while True:
            email = input("Enter your email to log in: ").strip()
            if self.logic.is_exist_email(email):
                self.params.append(email)
                print("Email exists.")
                break
            else:
                print("Email does not exist. Please register or try again.")

    def get_password_matched(self):
        while True:
            password = input("Enter your password: ").strip()
            email = self.params[-1]  # Retrieve the email added in the previous step
            if self.logic.is_exist_user(email, password):
                self.params.append(password)
                print("Password matched. Login successful.")
                break
            else:
                print("Incorrect password. Please try again.")


if __name__ == "__main__":
    user_facade = UserFacade()
    # user_facade.register_user()
    user_facade.login_user()
    print(user_facade.params)