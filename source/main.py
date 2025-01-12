from source.Facade.User_Facade import UserFacade
from source.Facade.Vacations_Facade import VacationFacade

class Main:
    def __init__(self):
        self.u_facade = UserFacade()
        self.v_facade = VacationFacade()

    def app_menu(self):
        while True:
            print("Welcome to Osher and Oron's vacation system!\nPlease choose what do to:")
            print("1 - Register new account")
            print("2 - Login")
            print("3 - Exit")
            select = input("Enter your selection here: ")
            if select == "1":
                self.u_facade.register_user()
            elif select == "2":
                self.u_facade.login_user()
            elif select == "3":
                return
            else:
                print("Invalid input! Please try again.")
                
                
if __name__ == "__main__":
    main = Main()
    main.app_menu()