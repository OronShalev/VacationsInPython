from source.Facade.User_Facade import UserFacade
from source.Facade.Vacations_Facade import VacationFacade
from source.Logic.User_Logic import UserLogic

class Main:
    def __init__(self):
        self.u_facade = UserFacade()
        self.u_logic = UserLogic()
        self.v_facade = VacationFacade()
        self.u_id = 0
        self.v_id = 0

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
                self.u_id = self.u_facade.params[0]
                if self.u_logic.is_admin(self.u_id):
                    self.__admin_menu()
                else:
                    self.__user_menu()

            elif select == "3":
                return
            else:
                print("Invalid input! Please try again.")

    def __admin_menu(self):
        pass

    def __user_menu(self):
        pass


if __name__ == "__main__":
    main = Main()
    main.app_menu()