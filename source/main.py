from source.Facade.User_Facade import UserFacade
from source.Facade.Vacations_Facade import VacationFacade
from source.Logic.User_Logic import UserLogic
from source.Logic.Vacations_Logic import VacationLogic
from source.Logic.Like_Logic import LikeLogic

class Main:
    def __init__(self):
        self.u_facade = UserFacade()
        self.u_logic = UserLogic()
        self.v_facade = VacationFacade()
        self.v_logic = VacationLogic()
        self.l_logic = LikeLogic()
        self.u_id = 0
        self.v_id = 0

    def app_menu(self):
        while True:
            print("\n\n\nWelcome to Osher and Oron's vacation system!\nPlease choose what do to:")
            print("1 - Register new account")
            print("2 - Login")
            print("3 - Exit")
            select = input("Enter your selection here: ")
            if select == "1":
                self.u_facade.register_user()
            elif select == "2":
                self.u_facade.login_user()
                user = self.u_logic.get_user_from_email_password(self.u_facade.params[0],  self.u_facade.params[1])
                self.u_id = user['id']
                input(f"Welcome {user['first_name']} {user['last_name']}, press enter to continue...")
                if self.u_logic.is_admin(self.u_id):
                    self.__admin_menu()
                else:
                    self.__user_menu()

            elif select == "3":
                return
            else:
                print("Invalid input! Please try again.")

    def __admin_menu(self):
        while True:
            print("\n\n\nAdmin Menu:")
            print("1 - View all Vacations")
            print("2 - Add vacation")
            print("3 - logout")
            select = input("Enter your selection here: ")
            if select == "1":
                self.__admin_vacations_menu()
            elif select == "2":
                self.v_facade.add_vacation()
            elif select == "3":
                self.u_facade.logout_user()
                return
            else:
                print("Invalid input! Please try again.")

    def __admin_vacations_menu(self):
        print("\n\n\nVacations view")
        print("Press 0 for admin menu")
        vacations = self.v_logic.get_all_vacations()
        count = 1
        for vac in vacations:
            print(f"Vacation {count}: {vac['vacation_title']} ,press {count} for more details")
            print(f"Likes: {len(self.l_logic.get_all_likes_by_vacation(vac["id"]))}")
            count = count + 1
        num = 0
        while True:
            vnum = input("Enter your selection here: ")
            try:
                num = int(vnum)
                if num == 0:
                    return
                if num < 1 or num > count:
                    print("Invalid input, please try again...")
                else:
                    break
            except:
                print(f"Input must be an integer, please try again...")
        self.v_id = vacations[num-1]['id']
        self.__admin_vac_show()

    def __admin_vac_show(self):
        print("\n\n")
        self.v_facade.show_vacation(self.v_id)
        print("Vacation actions")
        print("1 - Edit vacation")
        print("2 - Delete vacation")
        print("3 - Back")
        while True:
            select = input("Enter your selection here: ")
            if select == "1":
                self.v_facade.edit_vacation(self.v_id)
                self.__admin_vac_show()
                break
            elif select == "2":
                self.v_logic.del_vacation(self.v_id)
                self.__admin_vacations_menu()
                break
            elif select == "3":
                self.__admin_vacations_menu()
                break
            else:
                print("Invalid input! Please try again.")



    def __user_menu(self):
        while True:
            print("\n\n\nUser Menu:")
            print("1 - View all Vacations")
            print("2 - View liked vacations")
            print("3 - logout")
            select = input("Enter your selection here: ")
            if select == "1":
                self.__user_vacations_menu()
            elif select == "2":
                if len(self.l_logic.get_all_likes_by_user(self.u_id)) == 0:
                    print("No Liked vacations...")
                    continue
                self.__user_vacations_menu(True)
            elif select == "3":
                self.u_facade.logout_user()
                return
            else:
                print("Invalid input! Please try again.")

    def __user_vacations_menu(self, is_liked = False):
        print("\n\n\nVacations view")
        print("Press 0 for user menu")
        if is_liked:
            vacations = self.v_logic.get_all_vacations_liked_by_uid(self.u_id)
        else:
            vacations = self.v_logic.get_all_vacations()
        count = 1
        for vac in vacations:
            print(f"Vacation {count}: {vac['vacation_title']} ,press {count} for more details")
            print(f"Likes: {len(self.l_logic.get_all_likes_by_vacation(vac["id"]))}")
            print(f"Is Liked: {self.l_logic.is_liked(self.u_id, vac["id"])}")
            count = count + 1
        num = 0
        while True:
            vnum = input("Enter your selection here: ")
            try:
                num = int(vnum)
                print(num)
                if num == 0:
                    return
                if num < 1 or num > count:
                    print("Invalid input, please try again...")
                else:
                    break
            except:
                print(f"Input must be an integer, please try again...")
        self.v_id = vacations[num-1]['id']
        self.__user_vac_show()

    def __user_vac_show(self):
        print("\n\n")
        self.v_facade.show_vacation(self.v_id)
        like_status = self.l_logic.is_liked(self.u_id, self.v_id)
        print(like_status)
        print("Vacation actions")
        if like_status:
            print("1 - Unlike")
        else:
            print("1 - Like")
        print("2 - Back")
        while True:
            select = input("Enter your selection here: ")
            if select == "1":
                if like_status:
                    self.l_logic.remove_like(self.v_id, self.u_id)
                else:
                    self.l_logic.add_like(self.v_id, self.u_id)
                self.__user_vac_show()
                break
            elif select == "2":
                self.__user_vacations_menu()
                break
            else:
                print("Invalid input! Please try again.")


if __name__ == "__main__":
    main = Main()
    main.app_menu()