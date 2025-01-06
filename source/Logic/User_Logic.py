from source.Utils.DAL import DAL


class UserLogic:
    def __init__(self):
        self.dal = DAL()

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.dal.close()

    def get_all_users(self):
        query = "SELECT * from mydb.users"
        result = self.dal.get_table(query)
        return result if result is not None else []

    def is_admin(self, id):
        pass


    def add_user(self, first_name, last_name, email, password, date_of_birth):
        pass
        try:
            query = """
            INSERT INTO mydb.vacations 
            (vacation_title, desc, start_date, end_date, Countries_id, price, img_url)
            VALUES 
            (%s, %s, %s, %s, (SELECT id FROM mydb.Countries WHERE country_name LIKE %s), %s, %s)
            """
            params = (vacation_title, desc, start_date,
                    end_date, f"%{countries_name}%", price, img_url)
            self.dal.insert(query, params)
            return True


        except Exception as err:
            print(f"Error adding vacation: {err}")
            return False

    def is_exist_user(self, email, password):
        pass

    def is_exist_email(self, email):
        pass




if __name__ == "__main__":
    try:
        with UserLogic() as user_logic:
            users = user_logic.get_all_users()
            for user in users:
                print("----------------------")
                print(user)
    except Exception as err:
        print(f"Error: {err}")