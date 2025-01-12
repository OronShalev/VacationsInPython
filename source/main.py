from source.Facade.User_Facade import user_facade
from source.Facade.Vacations_Facade import vacation

class Main:
    def __init__(self):
        self.u_facade = user_facade()
        self.v_facade = vacation()

    def app_menu(self):
        while True:
            print("Wellcome to Osher and Oron's vacation system:"
                  "press 1 to ")